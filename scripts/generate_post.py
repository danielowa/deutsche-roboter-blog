#!/usr/bin/env python3
"""Daily robotics blog post generator.

Four-phase pipeline:
1. FETCH  - Pull recent articles from RSS feeds
2. ANALYZE - Claude selects the best topic
3. WRITE  - Claude writes a deep-dive article in German
4. PUBLISH - Generate Hugo markdown, git commit & push
"""

import argparse
import os
import re
import subprocess
import sys
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import anthropic
import feedparser
import yaml
from config import (
    ARTICLE_WRITING_PROMPT,
    ARTICLE_WRITING_SYSTEM,
    FETCH_TIMEOUT,
    MAX_ARTICLES_PER_FEED,
    MAX_TOTAL_ARTICLES,
    MODEL,
    RSS_FEEDS,
    TOPIC_SELECTION_PROMPT,
    TOPIC_SELECTION_SYSTEM,
)

# Project root (one level up from scripts/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = PROJECT_ROOT / "content" / "posts"

# Timezone for Berlin (handles CET/CEST automatically)
BERLIN_TZ = ZoneInfo("Europe/Berlin")


def get_today_str() -> str:
    """Return today's date as YYYY-MM-DD in Berlin time."""
    return datetime.now(BERLIN_TZ).strftime("%Y-%m-%d")


def post_exists_for_today() -> bool:
    """Check if a post for today already exists."""
    today = get_today_str()
    return any(CONTENT_DIR.glob(f"{today}-*.md"))


def get_recent_titles(days: int = 7) -> list[str]:
    """Read titles from the most recent posts to avoid duplicate topics."""
    titles = []
    for md_file in sorted(CONTENT_DIR.glob("*.md"), reverse=True):
        if md_file.name == "_index.md":
            continue
        try:
            text = md_file.read_text(encoding="utf-8")
            # Extract title from YAML frontmatter
            fm_match = re.search(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
            if fm_match:
                fm = yaml.safe_load(fm_match.group(1))
                if isinstance(fm, dict) and fm.get("title"):
                    titles.append(fm["title"])
        except Exception:
            continue
        if len(titles) >= days:
            break
    return titles


# ---------------------------------------------------------------------------
# Phase 1: FETCH
# ---------------------------------------------------------------------------


def fetch_rss_feeds() -> list[dict]:
    """Fetch articles from all configured RSS feeds.

    Individual feed failures are logged but don't block the pipeline.
    """
    all_articles = []

    for feed_cfg in RSS_FEEDS:
        name = feed_cfg["name"]
        url = feed_cfg["url"]
        try:
            print(f"  Fetching {name}...")
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "DeutscheRoboterBlog/1.0"},
            )
            with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
                raw_feed = resp.read()
            feed = feedparser.parse(raw_feed)
            if feed.bozo and not feed.entries:
                print(f"  WARNING: {name} returned no entries (bozo={feed.bozo})")
                continue

            count = 0
            for entry in feed.entries[:MAX_ARTICLES_PER_FEED]:
                article = {
                    "source": name,
                    "title": entry.get("title", "").strip(),
                    "link": entry.get("link", ""),
                    "summary": (entry.get("summary") or entry.get("description") or "").strip(),
                    "published": entry.get("published", ""),
                }
                if article["title"]:
                    all_articles.append(article)
                    count += 1
            print(f"  OK: {count} articles from {name}")

        except Exception as e:
            print(f"  ERROR fetching {name}: {e}")

    # Deduplicate by title (case-insensitive)
    seen_titles = set()
    unique = []
    for a in all_articles:
        key = a["title"].lower()
        if key not in seen_titles:
            seen_titles.add(key)
            unique.append(a)

    # Limit total count
    unique = unique[:MAX_TOTAL_ARTICLES]
    print(f"\n  Total unique articles: {len(unique)}")
    return unique


def format_news_for_prompt(articles: list[dict]) -> str:
    """Format articles as numbered list for the Claude prompt."""
    lines = []
    for i, a in enumerate(articles, 1):
        summary = a["summary"][:200] + "..." if len(a["summary"]) > 200 else a["summary"]
        # Strip HTML tags from summary
        summary = re.sub(r"<[^>]+>", "", summary).strip()
        lines.append(f"{i}. [{a['source']}] {a['title']}\n   {summary}\n")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Phase 2: ANALYZE (topic selection)
# ---------------------------------------------------------------------------


def _build_recent_topics_block() -> str:
    """Build a prompt section listing recent titles to avoid duplicates."""
    recent = get_recent_titles(days=7)
    if not recent:
        return ""
    titles_list = "\n".join(f"- {t}" for t in recent)
    return (
        "WICHTIG: Die folgenden Themen wurden bereits in den letzten Tagen behandelt. "
        "Wähle ein ANDERES Thema, das sich deutlich davon unterscheidet:\n"
        f"{titles_list}\n\n"
    )


def select_topic(client: anthropic.Anthropic, articles: list[dict]) -> dict:
    """Use Claude to select the best topic from fetched news."""
    news_text = format_news_for_prompt(articles)
    recent_block = _build_recent_topics_block()
    prompt = TOPIC_SELECTION_PROMPT.format(
        news_items=news_text,
        recent_topics_block=recent_block,
    )

    print("  Asking Claude to select topic...")
    response = client.messages.create(
        model=MODEL,
        max_tokens=500,
        system=TOPIC_SELECTION_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )

    response_text = response.content[0].text

    # Extract YAML from response (may be wrapped in ```yaml ... ```)
    yaml_match = re.search(r"```yaml\s*\n(.*?)```", response_text, re.DOTALL)
    yaml_str = yaml_match.group(1) if yaml_match else response_text

    try:
        topic_data = yaml.safe_load(yaml_str)
        if not isinstance(topic_data, dict):
            raise ValueError(f"Expected dict, got {type(topic_data).__name__}")
    except (yaml.YAMLError, ValueError) as e:
        print(f"  WARNING: YAML parsing failed ({e}), attempting regex fallback...")
        topic_data = _parse_topic_fallback(response_text)

    print(f"  Selected topic: {topic_data.get('topic', 'UNKNOWN')}")
    return topic_data


def _parse_topic_fallback(text: str) -> dict:
    """Fallback parser that extracts topic fields via regex when YAML parsing fails."""

    def _extract(key: str) -> str:
        match = re.search(rf'{key}:\s*"?([^"\n]+)"?', text)
        return match.group(1).strip().strip('"') if match else ""

    # Extract list fields (sources, tags)
    def _extract_list(key: str) -> list[str]:
        block = re.search(rf"{key}:\s*\n((?:\s*-\s*.+\n?)+)", text)
        if not block:
            return []
        return [item.strip().strip('"').strip("'") for item in re.findall(r'-\s*"?([^"\n]+)"?', block.group(1))]

    return {
        "topic": _extract("topic") or "Robotik-News des Tages",
        "angle": _extract("angle"),
        "sources": _extract_list("sources"),
        "tags": _extract_list("tags") or ["Robotik"],
        "category": _extract("category") or "Allgemein",
    }


# ---------------------------------------------------------------------------
# Phase 3: WRITE
# ---------------------------------------------------------------------------


def write_article(client: anthropic.Anthropic, topic_data: dict, articles: list[dict]) -> str:
    """Use Claude to write a deep-dive article in German."""
    # Build source summaries from fetched articles that match selected sources
    selected_sources = [s.lower() for s in topic_data.get("sources", [])]
    summaries = []
    for a in articles:
        if any(src in a["title"].lower() for src in selected_sources) or any(
            a["title"].lower() in src for src in selected_sources
        ):
            summaries.append(f"- **{a['title']}** ({a['source']}): {a['summary']}")
    # If no exact matches, include top 5 articles as context
    if not summaries:
        for a in articles[:5]:
            summaries.append(f"- **{a['title']}** ({a['source']}): {a['summary']}")

    prompt = ARTICLE_WRITING_PROMPT.format(
        topic=topic_data.get("topic", ""),
        angle=topic_data.get("angle", ""),
        sources=", ".join(topic_data.get("sources", [])),
        source_summaries="\n".join(summaries) if summaries else "Keine weiteren Details verfügbar.",
    )

    print("  Asking Claude to write article...")
    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=ARTICLE_WRITING_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )

    article_text = response.content[0].text
    word_count = len(article_text.split())
    print(f"  Article written: ~{word_count} words")
    return article_text


# ---------------------------------------------------------------------------
# Phase 4: PUBLISH
# ---------------------------------------------------------------------------


def slugify(text: str) -> str:
    """Create a URL-friendly slug from German text."""
    # Transliterate common German characters
    replacements = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ß": "ss",
        "Ä": "Ae",
        "Ö": "Oe",
        "Ü": "Ue",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text).strip("-")
    text = re.sub(r"-+", "-", text)
    return text[:80]


def create_post(topic_data: dict, article_text: str) -> Path:
    """Generate Hugo markdown file with frontmatter."""
    today = get_today_str()
    title = topic_data.get("topic", "Robotik-News des Tages")
    slug = slugify(title)
    filename = f"{today}-{slug}.md"
    filepath = CONTENT_DIR / filename

    tags = topic_data.get("tags", ["Robotik"])
    category = topic_data.get("category", "Allgemein")

    # Build frontmatter
    frontmatter = {
        "title": title,
        "date": datetime.now(BERLIN_TZ).isoformat(timespec="seconds"),
        "draft": False,
        "tags": tags,
        "categories": [category],
        "summary": topic_data.get("angle", ""),
        "ShowToc": True,
        "TocOpen": False,
    }

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        f.write("---\n\n")
        f.write(article_text)
        f.write("\n")

    print(f"  Created: {filepath.relative_to(PROJECT_ROOT)}")
    return filepath


def git_commit_and_push(filepath: Path, title: str) -> None:
    """Commit the new post and push to remote."""
    rel_path = filepath.relative_to(PROJECT_ROOT)

    subprocess.run(
        ["git", "add", str(rel_path)],
        cwd=PROJECT_ROOT,
        check=True,
    )

    today = get_today_str()
    commit_msg = f"post: {today} - {title}"
    subprocess.run(
        ["git", "commit", "-m", commit_msg],
        cwd=PROJECT_ROOT,
        check=True,
    )

    subprocess.run(
        ["git", "push"],
        cwd=PROJECT_ROOT,
        check=True,
    )
    print("  Pushed to remote.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Generate a daily robotics blog post.")
    parser.add_argument(
        "--no-git",
        action="store_true",
        help="Skip git commit and push (useful when running inside CI)",
    )
    return parser.parse_args()


def main() -> int:
    """Run the four-phase pipeline."""
    args = parse_args()

    print(f"\n{'=' * 60}")
    print("Deutsche Roboter Blog - Post Generator")
    print(f"Date: {get_today_str()}")
    print(f"{'=' * 60}\n")

    # Check for duplicate
    if post_exists_for_today():
        print("A post for today already exists. Skipping.")
        return 0

    # Require API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        return 1

    client = anthropic.Anthropic()

    # Phase 1: FETCH
    print("[1/4] Fetching RSS feeds...")
    articles = fetch_rss_feeds()
    if not articles:
        print("ERROR: No articles fetched from any source.")
        return 1

    # Phase 2: ANALYZE
    print("\n[2/4] Selecting topic...")
    topic_data = select_topic(client, articles)
    if not topic_data or not topic_data.get("topic"):
        print("ERROR: Claude did not return a valid topic.")
        return 1

    # Phase 3: WRITE
    print("\n[3/4] Writing article...")
    article_text = write_article(client, topic_data, articles)
    if not article_text:
        print("ERROR: Claude did not return an article.")
        return 1

    # Phase 4: PUBLISH
    print("\n[4/4] Publishing...")
    filepath = create_post(topic_data, article_text)

    if args.no_git:
        print("  --no-git: skipping git commit and push.")
    else:
        try:
            git_commit_and_push(filepath, topic_data.get("topic", ""))
        except subprocess.CalledProcessError as e:
            print(f"  WARNING: Git operation failed: {e}")
            print("  The post was created locally but not pushed.")
            return 1

    print("\nDone! Post published successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

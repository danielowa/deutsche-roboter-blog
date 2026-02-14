"""Tests for generate_post.py pure functions."""

from unittest.mock import patch

import yaml
from generate_post import (
    _build_recent_topics_block,
    create_post,
    format_news_for_prompt,
    get_recent_titles,
    post_exists_for_today,
    slugify,
)

# ---------------------------------------------------------------------------
# slugify()
# ---------------------------------------------------------------------------


class TestSlugify:
    def test_basic_text(self):
        assert slugify("Hello World") == "hello-world"

    def test_german_umlauts(self):
        assert slugify("Über Öffentliche Ärzte") == "ueber-oeffentliche-aerzte"

    def test_eszett(self):
        assert slugify("Straße") == "strasse"

    def test_uppercase_umlauts(self):
        assert slugify("Ärger Über Öl") == "aerger-ueber-oel"

    def test_special_characters_removed(self):
        assert slugify("Hello! @World #2024") == "hello-world-2024"

    def test_multiple_spaces_collapsed(self):
        assert slugify("Hello   World") == "hello-world"

    def test_multiple_hyphens_collapsed(self):
        assert slugify("Hello---World") == "hello-world"

    def test_leading_trailing_hyphens_stripped(self):
        assert slugify("--Hello World--") == "hello-world"

    def test_truncation_at_80_chars(self):
        long_text = "a" * 100
        result = slugify(long_text)
        assert len(result) <= 80

    def test_empty_string(self):
        assert slugify("") == ""

    def test_all_special_chars(self):
        assert slugify("!!!???") == ""

    def test_mixed_german_and_english(self):
        assert slugify("Künstliche Intelligenz und Robotik") == "kuenstliche-intelligenz-und-robotik"

    def test_underscores_removed(self):
        # Underscores are stripped by the special-char regex before the space-to-hyphen step
        assert slugify("hello_world_test") == "helloworldtest"


# ---------------------------------------------------------------------------
# format_news_for_prompt()
# ---------------------------------------------------------------------------


class TestFormatNewsForPrompt:
    def test_single_article(self):
        articles = [
            {
                "source": "TestSource",
                "title": "Test Title",
                "summary": "Short summary",
            }
        ]
        result = format_news_for_prompt(articles)
        assert "1. [TestSource] Test Title" in result
        assert "Short summary" in result

    def test_numbering(self):
        articles = [
            {"source": "A", "title": "First", "summary": "s1"},
            {"source": "B", "title": "Second", "summary": "s2"},
            {"source": "C", "title": "Third", "summary": "s3"},
        ]
        result = format_news_for_prompt(articles)
        assert "1. [A] First" in result
        assert "2. [B] Second" in result
        assert "3. [C] Third" in result

    def test_summary_truncation_at_200_chars(self):
        long_summary = "x" * 250
        articles = [{"source": "S", "title": "T", "summary": long_summary}]
        result = format_news_for_prompt(articles)
        # The truncated summary should be first 200 chars + "..."
        assert "x" * 200 + "..." in result
        assert "x" * 201 not in result

    def test_summary_not_truncated_at_200(self):
        summary = "x" * 200
        articles = [{"source": "S", "title": "T", "summary": summary}]
        result = format_news_for_prompt(articles)
        assert "..." not in result

    def test_html_tags_stripped(self):
        articles = [
            {
                "source": "S",
                "title": "T",
                "summary": "Hello <b>bold</b> and <a href='x'>link</a> text",
            }
        ]
        result = format_news_for_prompt(articles)
        assert "<b>" not in result
        assert "<a " not in result
        assert "</a>" not in result
        assert "bold" in result
        assert "link" in result

    def test_empty_articles_list(self):
        result = format_news_for_prompt([])
        assert result == ""


# ---------------------------------------------------------------------------
# post_exists_for_today()
# ---------------------------------------------------------------------------


class TestPostExistsForToday:
    def test_returns_true_when_post_exists(self, tmp_path):
        posts_dir = tmp_path / "content" / "posts"
        posts_dir.mkdir(parents=True)
        (posts_dir / "2026-02-14-test-post.md").write_text("content")

        with (
            patch("generate_post.CONTENT_DIR", posts_dir),
            patch("generate_post.get_today_str", return_value="2026-02-14"),
        ):
            assert post_exists_for_today() is True

    def test_returns_false_when_no_post(self, tmp_path):
        posts_dir = tmp_path / "content" / "posts"
        posts_dir.mkdir(parents=True)

        with (
            patch("generate_post.CONTENT_DIR", posts_dir),
            patch("generate_post.get_today_str", return_value="2026-02-14"),
        ):
            assert post_exists_for_today() is False

    def test_returns_false_for_different_date(self, tmp_path):
        posts_dir = tmp_path / "content" / "posts"
        posts_dir.mkdir(parents=True)
        (posts_dir / "2026-02-13-old-post.md").write_text("content")

        with (
            patch("generate_post.CONTENT_DIR", posts_dir),
            patch("generate_post.get_today_str", return_value="2026-02-14"),
        ):
            assert post_exists_for_today() is False


# ---------------------------------------------------------------------------
# get_recent_titles() / _build_recent_topics_block()
# ---------------------------------------------------------------------------


class TestGetRecentTitles:
    def _write_post(self, posts_dir, filename, title):
        (posts_dir / filename).write_text(
            f'---\ntitle: "{title}"\ndate: 2026-02-14T10:00:00+01:00\n'
            f"tags: [Robotik]\ncategories: [Industrie]\nsummary: test\n---\n\n## Heading\n\n{'word ' * 500}\n",
            encoding="utf-8",
        )

    def test_reads_titles_from_posts(self, tmp_path):
        posts_dir = tmp_path / "content" / "posts"
        posts_dir.mkdir(parents=True)
        self._write_post(posts_dir, "2026-02-14-post-a.md", "Post A")
        self._write_post(posts_dir, "2026-02-13-post-b.md", "Post B")

        with patch("generate_post.CONTENT_DIR", posts_dir):
            titles = get_recent_titles(days=7)
        assert "Post A" in titles
        assert "Post B" in titles

    def test_skips_index_md(self, tmp_path):
        posts_dir = tmp_path / "content" / "posts"
        posts_dir.mkdir(parents=True)
        (posts_dir / "_index.md").write_text("---\ntitle: Index\n---\n")
        self._write_post(posts_dir, "2026-02-14-post-a.md", "Post A")

        with patch("generate_post.CONTENT_DIR", posts_dir):
            titles = get_recent_titles(days=7)
        assert titles == ["Post A"]

    def test_limits_to_days_param(self, tmp_path):
        posts_dir = tmp_path / "content" / "posts"
        posts_dir.mkdir(parents=True)
        for i in range(5):
            self._write_post(posts_dir, f"2026-02-{14 - i:02d}-post.md", f"Post {i}")

        with patch("generate_post.CONTENT_DIR", posts_dir):
            titles = get_recent_titles(days=3)
        assert len(titles) == 3

    def test_empty_dir_returns_empty(self, tmp_path):
        posts_dir = tmp_path / "content" / "posts"
        posts_dir.mkdir(parents=True)

        with patch("generate_post.CONTENT_DIR", posts_dir):
            assert get_recent_titles(days=7) == []


class TestBuildRecentTopicsBlock:
    def test_empty_when_no_posts(self):
        with patch("generate_post.get_recent_titles", return_value=[]):
            assert _build_recent_topics_block() == ""

    def test_includes_titles_when_present(self):
        with patch("generate_post.get_recent_titles", return_value=["Title A", "Title B"]):
            block = _build_recent_topics_block()
            assert "WICHTIG" in block
            assert "Title A" in block
            assert "Title B" in block
            assert "ANDERES Thema" in block


# ---------------------------------------------------------------------------
# create_post()
# ---------------------------------------------------------------------------


class TestCreatePost:
    def _make_topic_data(self):
        return {
            "topic": "Neue Roboter für die Industrie",
            "angle": "Wie Roboter die Fertigung verändern",
            "tags": ["Robotik", "Industrie"],
            "category": "Industrie",
            "sources": ["Source A", "Source B"],
        }

    def test_creates_file_with_correct_name_pattern(self, tmp_path):
        posts_dir = tmp_path / "content" / "posts"
        topic_data = self._make_topic_data()

        with (
            patch("generate_post.CONTENT_DIR", posts_dir),
            patch("generate_post.PROJECT_ROOT", tmp_path),
            patch("generate_post.get_today_str", return_value="2026-02-14"),
        ):
            filepath = create_post(topic_data, "Article body here.")

        assert filepath.name.startswith("2026-02-14-")
        assert filepath.name.endswith(".md")
        assert filepath.exists()

    def test_frontmatter_has_required_fields(self, tmp_path):
        posts_dir = tmp_path / "content" / "posts"
        topic_data = self._make_topic_data()

        with (
            patch("generate_post.CONTENT_DIR", posts_dir),
            patch("generate_post.PROJECT_ROOT", tmp_path),
            patch("generate_post.get_today_str", return_value="2026-02-14"),
        ):
            filepath = create_post(topic_data, "Article body here.")

        content = filepath.read_text(encoding="utf-8")
        # Parse frontmatter between --- delimiters
        parts = content.split("---", 2)
        assert len(parts) >= 3, "File should have YAML frontmatter between --- delimiters"
        frontmatter = yaml.safe_load(parts[1])

        assert frontmatter["title"] == "Neue Roboter für die Industrie"
        assert frontmatter["draft"] is False
        assert frontmatter["tags"] == ["Robotik", "Industrie"]
        assert frontmatter["categories"] == ["Industrie"]
        assert frontmatter["summary"] == "Wie Roboter die Fertigung verändern"
        assert frontmatter["ShowToc"] is True
        assert frontmatter["TocOpen"] is False
        assert "date" in frontmatter

    def test_article_body_in_content(self, tmp_path):
        posts_dir = tmp_path / "content" / "posts"
        topic_data = self._make_topic_data()
        article_text = "## Einleitung\n\nDies ist der Artikeltext."

        with (
            patch("generate_post.CONTENT_DIR", posts_dir),
            patch("generate_post.PROJECT_ROOT", tmp_path),
            patch("generate_post.get_today_str", return_value="2026-02-14"),
        ):
            filepath = create_post(topic_data, article_text)

        content = filepath.read_text(encoding="utf-8")
        assert "## Einleitung" in content
        assert "Dies ist der Artikeltext." in content

    def test_default_values_when_topic_data_minimal(self, tmp_path):
        posts_dir = tmp_path / "content" / "posts"
        topic_data = {}  # No keys at all

        with (
            patch("generate_post.CONTENT_DIR", posts_dir),
            patch("generate_post.PROJECT_ROOT", tmp_path),
            patch("generate_post.get_today_str", return_value="2026-02-14"),
        ):
            filepath = create_post(topic_data, "Body text.")

        content = filepath.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        frontmatter = yaml.safe_load(parts[1])

        assert frontmatter["title"] == "Robotik-News des Tages"
        assert frontmatter["tags"] == ["Robotik"]
        assert frontmatter["categories"] == ["Allgemein"]

    def test_slug_used_in_filename(self, tmp_path):
        posts_dir = tmp_path / "content" / "posts"
        topic_data = {"topic": "Über Künstliche Intelligenz"}

        with (
            patch("generate_post.CONTENT_DIR", posts_dir),
            patch("generate_post.PROJECT_ROOT", tmp_path),
            patch("generate_post.get_today_str", return_value="2026-02-14"),
        ):
            filepath = create_post(topic_data, "Body.")

        assert "ueber-kuenstliche-intelligenz" in filepath.name

#!/usr/bin/env python3
"""Validate Hugo markdown posts for the Deutsche Roboter Blog.

Checks frontmatter integrity, content structure, and quality constraints.
Can be used as a standalone CLI tool or imported as a module.
"""

import re
import sys
from datetime import datetime
from pathlib import Path

import yaml


def validate_post(filepath: str | Path) -> list[str]:
    """Validate a Hugo markdown post file.

    Returns a list of error messages. Empty list means the post is valid.
    """
    filepath = Path(filepath)
    errors: list[str] = []

    if not filepath.exists():
        return [f"File not found: {filepath}"]

    if not filepath.suffix == ".md":
        return [f"Not a markdown file: {filepath}"]

    content = filepath.read_text(encoding="utf-8")

    # Split frontmatter and body
    frontmatter, body, parse_errors = _parse_frontmatter(content)
    errors.extend(parse_errors)
    if frontmatter is None:
        return errors

    # Validate frontmatter fields
    errors.extend(_validate_required_fields(frontmatter))
    errors.extend(_validate_date(frontmatter))
    errors.extend(_validate_list_fields(frontmatter))
    errors.extend(_validate_summary(frontmatter))

    # Validate body content
    errors.extend(_validate_word_count(body))
    errors.extend(_validate_headings(body))
    errors.extend(_validate_no_raw_html(body))

    return errors


def _parse_frontmatter(content: str) -> tuple[dict | None, str, list[str]]:
    """Parse YAML frontmatter from Hugo markdown content.

    Returns (frontmatter_dict, body_text, errors).
    """
    match = re.match(r"^---\n(.*?\n)---\n?(.*)", content, re.DOTALL)
    if not match:
        return None, "", ["Missing YAML frontmatter (no --- delimiters found)"]

    yaml_str = match.group(1)
    body = match.group(2).strip()

    try:
        frontmatter = yaml.safe_load(yaml_str)
    except yaml.YAMLError as e:
        return None, body, [f"YAML parsing error: {e}"]

    if not isinstance(frontmatter, dict):
        return None, body, [f"Frontmatter is not a mapping (got {type(frontmatter).__name__})"]

    return frontmatter, body, []


REQUIRED_FIELDS = ["title", "date", "tags", "categories", "summary"]


def _validate_required_fields(fm: dict) -> list[str]:
    """Check that all required frontmatter fields exist and are non-empty."""
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in fm:
            errors.append(f"Missing required field: {field}")
        elif fm[field] is None or (isinstance(fm[field], str) and not fm[field].strip()):
            errors.append(f"Empty required field: {field}")
    return errors


def _validate_date(fm: dict) -> list[str]:
    """Validate that the date field is a valid ISO 8601 datetime."""
    date_val = fm.get("date")
    if date_val is None:
        return []  # Already caught by required fields check

    # PyYAML may parse dates as datetime objects directly
    if isinstance(date_val, datetime):
        return []

    if not isinstance(date_val, str):
        return [f"Date field is not a string or datetime: {type(date_val).__name__}"]

    # Try parsing ISO 8601 formats
    # Covers: 2026-02-14T08:00:00+01:00, 2026-02-14T08:00:00+0100, 2026-02-14T08:00:00Z
    iso_pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}([+-]\d{2}:\d{2}|[+-]\d{4}|Z)$"
    if not re.match(iso_pattern, date_val):
        return [f"Invalid date format (expected ISO 8601 with timezone): {date_val}"]

    return []


def _validate_list_fields(fm: dict) -> list[str]:
    """Validate that tags and categories are non-empty lists."""
    errors = []
    for field in ("tags", "categories"):
        val = fm.get(field)
        if val is None:
            continue  # Already caught by required fields check
        if not isinstance(val, list):
            errors.append(f"Field '{field}' must be a list, got {type(val).__name__}")
        elif len(val) == 0:
            errors.append(f"Field '{field}' must have at least one entry")
    return errors


def _validate_summary(fm: dict) -> list[str]:
    """Validate summary length is between 50 and 300 characters."""
    summary = fm.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        return []  # Already caught by required fields check

    length = len(summary.strip())
    if length < 50:
        return [f"Summary too short ({length} chars, minimum 50)"]
    if length > 300:
        return [f"Summary too long ({length} chars, maximum 300)"]
    return []


MIN_WORD_COUNT = 400
MAX_WORD_COUNT = 2000


def _validate_word_count(body: str) -> list[str]:
    """Validate article body word count is within range."""
    words = body.split()
    count = len(words)
    if count < MIN_WORD_COUNT:
        return [f"Article too short ({count} words, minimum {MIN_WORD_COUNT})"]
    if count > MAX_WORD_COUNT:
        return [f"Article too long ({count} words, maximum {MAX_WORD_COUNT})"]
    return []


def _validate_headings(body: str) -> list[str]:
    """Validate that the article contains at least one ## heading."""
    if not re.search(r"^##\s+\S", body, re.MULTILINE):
        return ["Article must contain at least one ## heading"]
    return []


def _validate_no_raw_html(body: str) -> list[str]:
    """Warn if raw HTML tags are found in the body."""
    # Match HTML tags but ignore markdown image alt text and common false positives
    html_tags = re.findall(r"<(?!!)(/?\w[\w-]*)[^>]*>", body)
    if html_tags:
        unique_tags = sorted(set(html_tags))
        return [f"Raw HTML tags found (Hugo will strip these): {', '.join(unique_tags)}"]
    return []


def main() -> int:
    """CLI entry point: validate one or more post files."""
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file.md> [file2.md ...]", file=sys.stderr)
        return 1

    all_valid = True
    for path_str in sys.argv[1:]:
        filepath = Path(path_str)
        errors = validate_post(filepath)
        if errors:
            all_valid = False
            print(f"FAIL: {filepath}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK: {filepath}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())

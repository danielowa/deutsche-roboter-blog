"""Tests for validate_post.py validation rules."""

import textwrap
from pathlib import Path

import pytest
from validate_post import validate_post


def _write_post(tmp_path, frontmatter="", body="", filename="2026-02-14-test.md"):
    """Helper to write a test markdown file and return its path."""
    filepath = tmp_path / filename
    filepath.write_text(f"---\n{frontmatter}---\n\n{body}\n", encoding="utf-8")
    return filepath


def _valid_frontmatter():
    return textwrap.dedent("""\
        title: "Test Artikel über Robotik"
        date: 2026-02-14T08:00:00+01:00
        draft: false
        tags:
          - Robotik
          - Test
        categories:
          - Forschung
        summary: "Dies ist eine Zusammenfassung die lang genug ist um die Mindestlaenge zu erreichen."
    """)


def _valid_body():
    """Generate a valid article body with headings and enough words."""
    paragraphs = [
        "## Einleitung\n",
        "Die Robotik entwickelt sich rasant weiter. " * 30,
        "\n## Hauptteil\n",
        "Neue Forschungsergebnisse zeigen interessante Entwicklungen. " * 30,
        "\n## Fazit\n",
        "Die Zukunft der Robotik bleibt spannend und vielversprechend. " * 15,
    ]
    return "\n".join(paragraphs)


# ---------------------------------------------------------------------------
# File-level checks
# ---------------------------------------------------------------------------


class TestFileChecks:
    def test_file_not_found(self, tmp_path):
        errors = validate_post(tmp_path / "nonexistent.md")
        assert len(errors) == 1
        assert "File not found" in errors[0]

    def test_not_a_markdown_file(self, tmp_path):
        filepath = tmp_path / "test.txt"
        filepath.write_text("content")
        errors = validate_post(filepath)
        assert len(errors) == 1
        assert "Not a markdown file" in errors[0]


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------


class TestFrontmatterParsing:
    def test_valid_post_passes(self, tmp_path):
        filepath = _write_post(tmp_path, _valid_frontmatter(), _valid_body())
        errors = validate_post(filepath)
        assert errors == []

    def test_missing_frontmatter_delimiters(self, tmp_path):
        filepath = tmp_path / "test.md"
        filepath.write_text("No frontmatter here\n\nJust body text.", encoding="utf-8")
        errors = validate_post(filepath)
        assert any("Missing YAML frontmatter" in e for e in errors)

    def test_invalid_yaml(self, tmp_path):
        filepath = _write_post(tmp_path, "title: [invalid yaml\n", _valid_body())
        errors = validate_post(filepath)
        assert any("YAML parsing error" in e for e in errors)

    def test_frontmatter_not_a_dict(self, tmp_path):
        filepath = _write_post(tmp_path, "- just\n- a\n- list\n", _valid_body())
        errors = validate_post(filepath)
        assert any("not a mapping" in e for e in errors)


# ---------------------------------------------------------------------------
# Required fields
# ---------------------------------------------------------------------------


class TestRequiredFields:
    @pytest.mark.parametrize("field", ["title", "date", "tags", "categories", "summary"])
    def test_missing_required_field(self, tmp_path, field):
        fm = _valid_frontmatter()
        # Remove the field line (and any continuation lines for lists)
        lines = fm.splitlines(keepends=True)
        filtered = []
        skip_indented = False
        for line in lines:
            if line.startswith(f"{field}:"):
                skip_indented = True
                continue
            if skip_indented and line.startswith("  "):
                continue
            skip_indented = False
            filtered.append(line)
        fm_without_field = "".join(filtered)

        filepath = _write_post(tmp_path, fm_without_field, _valid_body())
        errors = validate_post(filepath)
        assert any(f"Missing required field: {field}" in e for e in errors)

    def test_empty_title(self, tmp_path):
        fm = _valid_frontmatter().replace('title: "Test Artikel über Robotik"', 'title: ""')
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert any("Empty required field: title" in e for e in errors)

    def test_null_title(self, tmp_path):
        fm = _valid_frontmatter().replace('title: "Test Artikel über Robotik"', "title:")
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert any("Empty required field: title" in e for e in errors)


# ---------------------------------------------------------------------------
# Date validation
# ---------------------------------------------------------------------------


class TestDateValidation:
    def test_valid_iso_date_with_offset(self, tmp_path):
        filepath = _write_post(tmp_path, _valid_frontmatter(), _valid_body())
        errors = validate_post(filepath)
        assert not any("date" in e.lower() for e in errors)

    def test_valid_iso_date_with_z(self, tmp_path):
        fm = _valid_frontmatter().replace("date: 2026-02-14T08:00:00+01:00", "date: 2026-02-14T08:00:00Z")
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert not any("Invalid date" in e for e in errors)

    def test_invalid_date_format(self, tmp_path):
        fm = _valid_frontmatter().replace("date: 2026-02-14T08:00:00+01:00", 'date: "February 14, 2026"')
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert any("Invalid date format" in e for e in errors)

    def test_date_without_timezone(self, tmp_path):
        fm = _valid_frontmatter().replace("date: 2026-02-14T08:00:00+01:00", 'date: "2026-02-14T08:00:00"')
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert any("Invalid date format" in e for e in errors)


# ---------------------------------------------------------------------------
# List fields (tags, categories)
# ---------------------------------------------------------------------------


class TestListFields:
    def test_tags_not_a_list(self, tmp_path):
        fm = _valid_frontmatter().replace("tags:\n  - Robotik\n  - Test", 'tags: "just a string"')
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert any("'tags' must be a list" in e for e in errors)

    def test_categories_not_a_list(self, tmp_path):
        fm = _valid_frontmatter().replace("categories:\n  - Forschung", 'categories: "just a string"')
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert any("'categories' must be a list" in e for e in errors)

    def test_empty_tags_list(self, tmp_path):
        fm = _valid_frontmatter().replace("tags:\n  - Robotik\n  - Test", "tags: []")
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert any("'tags' must have at least one entry" in e for e in errors)

    def test_empty_categories_list(self, tmp_path):
        fm = _valid_frontmatter().replace("categories:\n  - Forschung", "categories: []")
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert any("'categories' must have at least one entry" in e for e in errors)


# ---------------------------------------------------------------------------
# Summary length
# ---------------------------------------------------------------------------


class TestSummaryLength:
    def test_summary_too_short(self, tmp_path):
        fm = _valid_frontmatter().replace(
            'summary: "Dies ist eine Zusammenfassung die lang genug ist um die Mindestlaenge zu erreichen."',
            'summary: "Zu kurz."',
        )
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert any("Summary too short" in e for e in errors)

    def test_summary_too_long(self, tmp_path):
        long_summary = "A" * 301
        fm = _valid_frontmatter().replace(
            'summary: "Dies ist eine Zusammenfassung die lang genug ist um die Mindestlaenge zu erreichen."',
            f'summary: "{long_summary}"',
        )
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert any("Summary too long" in e for e in errors)

    def test_summary_at_minimum_boundary(self, tmp_path):
        summary_50 = "A" * 50
        fm = _valid_frontmatter().replace(
            'summary: "Dies ist eine Zusammenfassung die lang genug ist um die Mindestlaenge zu erreichen."',
            f'summary: "{summary_50}"',
        )
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert not any("Summary too short" in e for e in errors)

    def test_summary_at_maximum_boundary(self, tmp_path):
        summary_300 = "A" * 300
        fm = _valid_frontmatter().replace(
            'summary: "Dies ist eine Zusammenfassung die lang genug ist um die Mindestlaenge zu erreichen."',
            f'summary: "{summary_300}"',
        )
        filepath = _write_post(tmp_path, fm, _valid_body())
        errors = validate_post(filepath)
        assert not any("Summary too long" in e for e in errors)


# ---------------------------------------------------------------------------
# Word count
# ---------------------------------------------------------------------------


class TestWordCount:
    def test_article_too_short(self, tmp_path):
        short_body = "## Heading\n\nJust a few words here."
        filepath = _write_post(tmp_path, _valid_frontmatter(), short_body)
        errors = validate_post(filepath)
        assert any("Article too short" in e for e in errors)

    def test_article_too_long(self, tmp_path):
        long_body = "## Heading\n\n" + "Wort " * 2001
        filepath = _write_post(tmp_path, _valid_frontmatter(), long_body)
        errors = validate_post(filepath)
        assert any("Article too long" in e for e in errors)

    def test_article_within_range(self, tmp_path):
        filepath = _write_post(tmp_path, _valid_frontmatter(), _valid_body())
        errors = validate_post(filepath)
        assert not any("Article too short" in e or "Article too long" in e for e in errors)


# ---------------------------------------------------------------------------
# Headings
# ---------------------------------------------------------------------------


class TestHeadings:
    def test_no_headings(self, tmp_path):
        body_no_headings = "Einfacher Text ohne Ueberschriften. " * 80
        filepath = _write_post(tmp_path, _valid_frontmatter(), body_no_headings)
        errors = validate_post(filepath)
        assert any("at least one ## heading" in e for e in errors)

    def test_has_h2_heading(self, tmp_path):
        filepath = _write_post(tmp_path, _valid_frontmatter(), _valid_body())
        errors = validate_post(filepath)
        assert not any("heading" in e for e in errors)

    def test_only_h1_heading_not_sufficient(self, tmp_path):
        body = "# Nur H1\n\n" + "Einiger Text hier. " * 80
        filepath = _write_post(tmp_path, _valid_frontmatter(), body)
        errors = validate_post(filepath)
        assert any("at least one ## heading" in e for e in errors)


# ---------------------------------------------------------------------------
# Raw HTML detection
# ---------------------------------------------------------------------------


class TestRawHTML:
    def test_no_html_is_clean(self, tmp_path):
        filepath = _write_post(tmp_path, _valid_frontmatter(), _valid_body())
        errors = validate_post(filepath)
        assert not any("Raw HTML" in e for e in errors)

    def test_detects_html_tags(self, tmp_path):
        body_with_html = "## Heading\n\n" + "Text " * 80 + "\n<div>Some HTML</div>\n" + "Mehr Text. " * 40
        filepath = _write_post(tmp_path, _valid_frontmatter(), body_with_html)
        errors = validate_post(filepath)
        assert any("Raw HTML tags found" in e for e in errors)

    def test_detects_multiple_html_tags(self, tmp_path):
        body = "## Heading\n\n" + "Text " * 60 + "\n<b>bold</b> and <a href='x'>link</a>\n" + "Mehr Text. " * 40
        filepath = _write_post(tmp_path, _valid_frontmatter(), body)
        errors = validate_post(filepath)
        assert any("Raw HTML tags found" in e for e in errors)


# ---------------------------------------------------------------------------
# Integration: valid post from existing content
# ---------------------------------------------------------------------------


class TestExistingPost:
    def test_welcome_post_is_valid(self):
        """Validate the actual welcome post in the repo."""
        filepath = (
            Path(__file__).resolve().parent.parent
            / "content"
            / "posts"
            / "2026-02-06-willkommen-beim-deutschen-roboter-blog.md"
        )
        if not filepath.exists():
            pytest.skip("Welcome post not found")
        errors = validate_post(filepath)
        # The welcome post is shorter than typical generated posts, so we allow word count errors
        non_wordcount_errors = [e for e in errors if "word" not in e.lower()]
        assert non_wordcount_errors == [], f"Unexpected errors: {non_wordcount_errors}"

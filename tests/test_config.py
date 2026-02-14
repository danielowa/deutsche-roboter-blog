"""Tests for config.py validation."""

from urllib.parse import urlparse

from config import (
    ARTICLE_WRITING_PROMPT,
    FETCH_TIMEOUT,
    MAX_ARTICLES_PER_FEED,
    MAX_TOTAL_ARTICLES,
    MODEL,
    RSS_FEEDS,
    TOPIC_SELECTION_PROMPT,
)


class TestRSSFeeds:
    def test_feeds_is_non_empty_list(self):
        assert isinstance(RSS_FEEDS, list)
        assert len(RSS_FEEDS) > 0

    def test_each_feed_has_name_and_url(self):
        for feed in RSS_FEEDS:
            assert "name" in feed, f"Feed missing 'name': {feed}"
            assert "url" in feed, f"Feed missing 'url': {feed}"

    def test_each_feed_name_is_non_empty_string(self):
        for feed in RSS_FEEDS:
            assert isinstance(feed["name"], str)
            assert len(feed["name"].strip()) > 0, f"Feed has empty name: {feed}"

    def test_each_feed_url_is_valid_https(self):
        for feed in RSS_FEEDS:
            parsed = urlparse(feed["url"])
            assert parsed.scheme == "https", f"Feed URL not HTTPS: {feed['url']}"
            assert parsed.netloc, f"Feed URL has no host: {feed['url']}"

    def test_no_duplicate_feed_names(self):
        names = [f["name"] for f in RSS_FEEDS]
        assert len(names) == len(set(names)), "Duplicate feed names found"

    def test_no_duplicate_feed_urls(self):
        urls = [f["url"] for f in RSS_FEEDS]
        assert len(urls) == len(set(urls)), "Duplicate feed URLs found"


class TestPrompts:
    def test_topic_selection_prompt_has_news_items_placeholder(self):
        assert "{news_items}" in TOPIC_SELECTION_PROMPT

    def test_article_writing_prompt_has_required_placeholders(self):
        assert "{topic}" in ARTICLE_WRITING_PROMPT
        assert "{angle}" in ARTICLE_WRITING_PROMPT
        assert "{sources}" in ARTICLE_WRITING_PROMPT

    def test_topic_selection_prompt_is_non_empty(self):
        assert len(TOPIC_SELECTION_PROMPT.strip()) > 100

    def test_article_writing_prompt_is_non_empty(self):
        assert len(ARTICLE_WRITING_PROMPT.strip()) > 100


class TestConstants:
    def test_model_is_string(self):
        assert isinstance(MODEL, str)
        assert len(MODEL) > 0

    def test_model_starts_with_claude(self):
        assert MODEL.startswith("claude-"), f"MODEL should be a Claude model, got: {MODEL}"

    def test_max_articles_per_feed_is_positive(self):
        assert isinstance(MAX_ARTICLES_PER_FEED, int)
        assert MAX_ARTICLES_PER_FEED > 0

    def test_max_total_articles_is_positive(self):
        assert isinstance(MAX_TOTAL_ARTICLES, int)
        assert MAX_TOTAL_ARTICLES > 0

    def test_max_total_gte_max_per_feed(self):
        assert MAX_TOTAL_ARTICLES >= MAX_ARTICLES_PER_FEED

    def test_fetch_timeout_is_positive(self):
        assert isinstance(FETCH_TIMEOUT, int)
        assert FETCH_TIMEOUT > 0

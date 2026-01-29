"""Tests for scraper module."""

import pytest
from src.scraper.web_scraper import WebScraper


def test_scraper_init():
    """Test WebScraper initialization."""
    scraper = WebScraper()
    assert scraper.enable_search is False


def test_scraper_collect():
    """Test content collection."""
    scraper = WebScraper()
    content = scraper.collect("test topic", max_results=3)
    assert len(content) == 3
    assert "title" in content[0]
    assert "points" in content[0]

"""Tests for recommendation guardrails."""

from src.guardrails import validate_recommendations


def test_valid_recommendations_pass():
    recommendations = [
        (
            {"title": "Song A"},
            3.5,
            "Matches genre and energy preferences.",
        ),
        (
            {"title": "Song B"},
            3.0,
            "Matches mood preferences.",
        ),
        (
            {"title": "Song C"},
            2.5,
            "Matches acoustic preferences.",
        ),
    ]

    assert validate_recommendations(recommendations) == []


def test_detects_duplicate_titles():
    recommendations = [
        ({"title": "Song A"}, 3.5, "Good match."),
        ({"title": "Song A"}, 3.0, "Another match."),
        ({"title": "Song C"}, 2.5, "Good match."),
    ]

    errors = validate_recommendations(recommendations)

    assert any("Duplicate recommendation" in error for error in errors)


def test_detects_missing_explanation():
    recommendations = [
        ({"title": "Song A"}, 3.5, ""),
        ({"title": "Song B"}, 3.0, "Good match."),
        ({"title": "Song C"}, 2.5, "Good match."),
    ]

    errors = validate_recommendations(recommendations)

    assert any("Missing explanation" in error for error in errors)


def test_detects_too_few_results():
    recommendations = [
        ({"title": "Song A"}, 3.5, "Good match."),
    ]

    errors = validate_recommendations(recommendations)

    assert any("Expected at least" in error for error in errors)
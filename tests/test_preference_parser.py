"""Tests for the natural-language music preference parser."""

import pytest

from src.preference_parser import parse_music_request


def test_parses_workout_pop_request():
    preferences = parse_music_request(
        "I want upbeat pop music for a workout."
    )

    assert preferences["genre"] == "pop"
    assert preferences["mood"] == "energetic"
    assert preferences["energy"] == 0.9
    assert preferences["likes_acoustic"] is False


def test_parses_acoustic_study_request():
    preferences = parse_music_request(
        "Give me calm acoustic music for studying."
    )

    assert preferences["mood"] == "chill"
    assert preferences["energy"] == 0.3
    assert preferences["likes_acoustic"] is True


def test_uses_defaults_for_unknown_preferences():
    preferences = parse_music_request(
        "Give me something interesting."
    )

    assert preferences["genre"] == ""
    assert preferences["mood"] == ""
    assert preferences["energy"] == 0.5
    assert preferences["likes_acoustic"] is False


def test_rejects_empty_request():
    with pytest.raises(ValueError):
        parse_music_request("   ")


def test_rejects_non_string_request():
    with pytest.raises(TypeError):
        parse_music_request(123)
"""Reliability checks for VibeCheck AI recommendations."""

from math import isfinite
from typing import List, Tuple, Dict


def validate_recommendations(
    recommendations: List[Tuple[Dict, float, str]],
    minimum_results: int = 3,
) -> List[str]:
    """
    Check recommendation output for common reliability problems.

    Args:
        recommendations: Ranked recommendation tuples containing
            a song dictionary, score, and explanation.
        minimum_results: Minimum acceptable number of results.

    Returns:
        A list of error messages. An empty list means all checks passed.
    """
    errors = []

    if len(recommendations) < minimum_results:
        errors.append(
            f"Expected at least {minimum_results} recommendations, "
            f"but received {len(recommendations)}."
        )

    seen_titles = set()

    for song, score, explanation in recommendations:
        title = song.get("title", "").strip()

        if not title:
            errors.append("A recommendation is missing a song title.")
        elif title in seen_titles:
            errors.append(f"Duplicate recommendation found: {title}.")
        else:
            seen_titles.add(title)

        if not isinstance(score, (int, float)) or not isfinite(score):
            errors.append(f"Invalid score found for {title or 'unknown song'}.")

        if not isinstance(explanation, str) or not explanation.strip():
            errors.append(
                f"Missing explanation for {title or 'unknown song'}."
            )

    return errors
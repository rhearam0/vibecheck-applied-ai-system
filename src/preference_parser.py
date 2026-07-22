"""Parse natural-language music requests into structured preferences."""

from typing import Dict


def parse_music_request(request: str) -> Dict:
    """Convert a natural-language request into music preferences."""
    if not isinstance(request, str):
        raise TypeError("Music request must be text.")

    cleaned_request = request.strip().lower()

    if not cleaned_request:
        raise ValueError("Music request cannot be empty.")

    if len(cleaned_request) > 300:
        raise ValueError("Music request must be 300 characters or fewer.")

    preferences = {
        "genre": "",
        "mood": "",
        "energy": 0.5,
        "likes_acoustic": False,
    }

    genre_keywords = {
        "pop": ["pop"],
        "rock": ["rock", "guitar"],
        "hip-hop": ["hip-hop", "hip hop", "rap", "trap"],
        "jazz": ["jazz"],
        "electronic": ["electronic", "edm", "dance"],
        "folk": ["folk"],
        "country": ["country"],
        "r&b": ["r&b", "rnb"],
    }

    mood_keywords = {
        "happy": ["happy", "cheerful", "uplifting", "positive"],
        "sad": ["sad", "melancholy", "heartbreak", "emotional"],
        "chill": ["chill", "calm", "relaxing", "peaceful", "study"],
        "energetic": ["energetic", "exciting", "intense", "workout"],
    }

    for genre, keywords in genre_keywords.items():
        if any(keyword in cleaned_request for keyword in keywords):
            preferences["genre"] = genre
            break

    for mood, keywords in mood_keywords.items():
        if any(keyword in cleaned_request for keyword in keywords):
            preferences["mood"] = mood
            break

    high_energy_keywords = [
        "energetic",
        "upbeat",
        "workout",
        "gym",
        "intense",
        "fast",
        "party",
    ]

    low_energy_keywords = [
        "calm",
        "relaxing",
        "quiet",
        "slow",
        "study",
        "sleep",
        "peaceful",
    ]

    if any(keyword in cleaned_request for keyword in high_energy_keywords):
        preferences["energy"] = 0.9
    elif any(keyword in cleaned_request for keyword in low_energy_keywords):
        preferences["energy"] = 0.3

    acoustic_keywords = [
        "acoustic",
        "unplugged",
        "soft guitar",
        "natural instruments",
    ]

    if any(keyword in cleaned_request for keyword in acoustic_keywords):
        preferences["likes_acoustic"] = True

    return preferences
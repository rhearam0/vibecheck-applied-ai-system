"""
Command line runner for the VibeCheck AI music recommender.
"""

from pathlib import Path
import sys

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from preference_parser import parse_music_request
    from recommender import load_songs, recommend_songs
else:
    from .preference_parser import parse_music_request
    from .recommender import load_songs, recommend_songs


def print_profile_results(
    songs,
    profile_name: str,
    user_prefs: dict,
    k: int = 5,
) -> None:
    """Print ranked recommendations for one user profile."""
    print(f"\n=== {profile_name} ===")
    print(f"User preferences: {user_prefs}")

    recommendations = recommend_songs(user_prefs, songs, k=k)

    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec

        print(f"{index}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Why: {explanation}")
        print("-" * 40)


def main() -> None:
    """Run the interactive VibeCheck AI recommendation workflow."""
    project_root = Path(__file__).resolve().parent.parent
    songs_path = project_root / "data" / "songs.csv"
    songs = load_songs(str(songs_path))

    print("\n=== VibeCheck AI ===")

    request = input(
        "Describe the kind of music you're looking for:\n> "
    )

    try:
        parsed_preferences = parse_music_request(request)

        print("\nAI interpreted your request as:")
        print(parsed_preferences)

        print_profile_results(
            songs,
            "Your Personalized Recommendations",
            parsed_preferences,
        )

    except (TypeError, ValueError) as error:
        print(f"\nInput error: {error}")


if __name__ == "__main__":
    main()
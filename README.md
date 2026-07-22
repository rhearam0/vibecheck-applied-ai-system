#  🎵 VibeCheck AI: Applied Music Recommendation System

## Project Summary

VibeCheck AI extends my Module 3 Music Recommender Simulation into a complete Applied AI System. The original project recommended songs using structured user preferences such as genre, mood, energy, and acoustic preference. This upgraded version allows users to describe the type of music they want using natural language.

The system interprets a user's request, converts it into structured music preferences, retrieves relevant songs from the dataset, ranks them using a recommendation algorithm, explains why each song was selected, and validates the results using built-in reliability checks before displaying recommendations.

---
## AI Features 
This project extends the original recommender by integrating several AI-inspired components into one workflow.

Natural Language Preference Parsing

Instead of manually entering structured preferences, users can type requests such as:

I want upbeat pop music for a workout.

The system extracts music preferences including:

   - Genre
   - Mood
   - Energy level
   - Acoustic preference

These structured preferences are then passed directly into the recommendation engine.

Recommendation Engine

Each song is scored using multiple attributes including:

   - Genre
   - Mood
   - Energy
   - Acousticness

Songs that better match the user's preferences receive higher scores and are ranked from best to worst.

Reliability Guardrails

Before recommendations are displayed, the system automatically checks for:

   - Duplicate recommendations
   - Invalid recommendation scores
   - Missing song titles
   - Missing recommendation explanations
   - Too few recommendations returned

If any reliability checks fail, the user receives an error instead of potentially incorrect recommendations.

Evaluation Harness

The project also includes an automated evaluation script that tests multiple predefined music requests to verify that:

  - Natural-language parsing works correctly.
  - Recommendations are generated successfully.
  - Guardrails behave as expected.
  - Empty input is rejected safely.

---

## How the System Works 
This project is a content-based music recommender. The user starts by typing a request in natural language, such as "I want upbeat pop music for a workout." The system uses a preference parser to identify important information like genre, mood, energy level, and whether the user prefers acoustic music.

Once the preferences are identified, the recommender compares them to every song in the dataset. Each song is given a score based on how closely it matches the user's preferences. Songs with higher scores are ranked first and returned to the user along with an explanation of why they were recommended.

Before the recommendations are displayed, the system runs reliability checks to make sure there are no duplicate songs, missing explanations, invalid scores, or too few recommendations. An evaluation script is also included to test the system on several sample requests and verify that everything works correctly.

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python3 src/main.py
```

### Running Tests

Run the unit tests:

```bash
python3 -m pytest -v
```

### Running the Evaluation Script

Run the end-to-end evaluation:

```bash
python3 evaluation/evaluate_system.py
```
## Sample Recommendation Output

```text
=== VibeCheck AI ===

Describe the kind of music you're looking for:
> I want upbeat pop music for a workout.

AI interpreted your request as:

{
    "genre": "pop",
    "mood": "energetic",
    "energy": 0.9,
    "likes_acoustic": False
}

Reliability check: PASSED

=== Your Personalized Recommendations ===

1. Gym Hero by Max Pulse
   Score: 3.24
   Why: Matches your preferences: genre match (+1.0), energy similarity (+1.94), less acoustic (+0.3)

2. Sunrise City by Neon Echo
   Score: 3.14
   Why: Matches your preferences: genre match (+1.0), energy similarity (+1.84), less acoustic (+0.3)

3. Storm Runner by Voltline
   Score: 2.28
   Why: Matches your preferences: energy similarity (+1.98), less acoustic (+0.3)
```

---

## Experiments 
----------------------------------------

I tested the recommender using several different types of music requests to make sure the parser and recommendation engine behaved consistently.

Some example requests included:

- "I want upbeat pop music for a workout."
- "Give me calm acoustic music for studying."
- "I want relaxing songs before bed."
- "Give me something interesting."

I also tested invalid input, such as an empty request, to verify that the guardrails correctly rejected it. Finally, I used the evaluation script to automatically run several predefined test cases and confirm that the parser, recommender, and reliability checks worked together correctly.

---

## Limitations and Risks

This recommender has a few important limitations. It only works with a small catalog of songs, so the recommendations are not very broad or diverse. It also relies on a small set of features, which means it does not understand deeper things like lyrics, artist style, or cultural context. Because of that, it can overemphasize one genre or mood and make the results feel repetitive.

---

## Reflection

This project helped me better understand how recommendation systems work and how AI can be used to improve a simple application. My original recommender used structured user preferences, but I expanded it into a more complete AI system by adding a natural-language preference parser, reliability guardrails, and an evaluation script.

One thing I learned is that building an AI system is more than just generating recommendations. It's also important to make sure the system is reliable and produces consistent results. Adding automated tests and guardrails helped make the recommendations more trustworthy.

AI was very helpful throughout the project. It helped me brainstorm new features, debug problems, and create additional tests. At the same time, I learned that I couldn't accept every suggestion without checking it. Some suggestions introduced import errors or placed code in the wrong files, so I had to test everything and make corrections myself.

Overall, this project gave me a much better understanding of how recommendation systems, natural-language processing, and software testing all work together to create a reliable AI application.


# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Real-world recommendation systems use different types of data to figure out what users might want to listen to next. For example, Spotify looks at things like a user's listening history, liked songs, playlists, and the characteristics of the songs they listen to. In this project, I am building a **content-based recommender**, which means the system recommends songs by comparing a user's preferences to the features of each song instead of comparing them to other users.

For example, if a user mostly listens to pop music, the recommender can recognize that they prefer the **pop** genre and suggest other pop songs. It can also compare features like **energy** to recommend songs with a similar intensity and **tempo** to find songs with a similar pace. **Mood** is another important feature because it helps match the overall vibe of the music. Although the dataset includes other features like **acousticness**, my recommender will mainly use **genre, mood, energy, and tempo** because I think those features best describe the kind of music someone is looking for.

Here is the scoring model:

Start each song with a score of 0.

If the song genre matches the user's favorite genre:
add 2.0 points

If the song mood matches the user's favorite mood:
add 1.0 point

Add energy similarity:
1 - abs(song energy - target energy)

Add tempo similarity:
1 - abs(song tempo - target tempo) / 100

After scoring every song:
sort songs from highest score to lowest score
recommend the top songs

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output
Top recommendations:

1. Sunrise City
   Score: 4.28
   Why: Matches your preferences: genre match (+2.0), mood match (+1.0), energy similarity (+0.98), less acoustic (+0.3)
----------------------------------------
2. Gym Hero
   Score: 3.17
   Why: Matches your preferences: genre match (+2.0), energy similarity (+0.87), less acoustic (+0.3)
----------------------------------------
3. Rooftop Lights
   Score: 2.26
   Why: Matches your preferences: mood match (+1.0), energy similarity (+0.96), less acoustic (+0.3)
----------------------------------------
4. Neon Pulse
   Score: 1.26
   Why: Matches your preferences: energy similarity (+0.96), less acoustic (+0.3)
----------------------------------------
5. Night Drive Loop
   Score: 1.25
   Why: Matches your preferences: energy similarity (+0.95), less acoustic (+0.3)

---

## Experiments You Tried
----------------------------------------

#TERMINAL OUTPUT FOR EACH PROFILE RECCOMENDATION 
=== Trap profile ===
User preferences: {'genre': 'hip-hop', 'mood': 'sad', 'energy': 0.1, 'likes_acoustic': True}
1. Sunset Strings
   Score: 1.38
   Why: Matches your preferences: energy similarity (+0.88), acoustic preference (+0.5)
----------------------------------------
2. Spacewalk Thoughts
   Score: 1.32
   Why: Matches your preferences: energy similarity (+0.82), acoustic preference (+0.5)
----------------------------------------
3. Library Rain
   Score: 1.25
   Why: Matches your preferences: energy similarity (+0.75), acoustic preference (+0.5)
----------------------------------------
4. Blue Midnight
   Score: 1.25
   Why: Matches your preferences: energy similarity (+0.75), acoustic preference (+0.5)
----------------------------------------
5. Coffee Shop Stories
   Score: 1.23
   Why: Matches your preferences: energy similarity (+0.73), acoustic preference (+0.5)
----------------------------------------

---

## Limitations and Risks

This recommender has a few important limitations. It only works with a small catalog of songs, so the recommendations are not very broad or diverse. It also relies on a small set of features, which means it does not understand deeper things like lyrics, artist style, or cultural context. Because of that, it can overemphasize one genre or mood and make the results feel repetitive.

---

## Reflection

Recommenders turn data into predictions by looking at a user’s preferences and comparing them to the features of available items. In this project, that meant giving songs points based on things like genre, mood, energy, and acousticness, then ranking them to choose the best matches. I learned that even a simple recommender can make decisions that feel surprisingly personal, because it is using patterns in the data to guess what a user might enjoy next.

Bias and unfairness can show up in systems like this when they rely too heavily on a few obvious features or when the data itself is limited. If one genre or mood is overrepresented, the system may keep recommending similar songs and make other kinds of music less likely to appear. That is important because recommender systems can quietly shape what people discover, and that can limit variety or reinforce existing habits.

## Personal Reflection 
The biggest learning moment during the project was learning how much data is used when it comes to these platforms. When I use Spotify, I get a lot of good reccomendation songs but I never knew how much work is put behind the scenes in order to create those playlists and reccomednations. Using AI really helped me quickly experiment my reccomednation systems, and let me know what worked and what didnt along with showing me the use cases with various personas. Next time if I did this project again I would want to create a cool interface to see it come to life and have things like the artist playlist show, or a cool UI experience being developed. 


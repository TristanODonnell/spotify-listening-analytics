# Project Scope — Spotify Listening Analytics (v1)

## Duration
- Target duration: 7 days
- Hard stop: 10 days

## Deliverable Format
- Jupyter Notebook as the primary analysis medium
- Exported artifacts (charts and summary markdown) saved to disk

## Stop Conditions (Definition of Done)
The project is considered complete when all of the following are true:

- A data pipeline exists that produces a cleaned dataset saved to `data/processed/`
- Exploratory analysis includes at least 5 charts with written insights
- A Spotify Wrapped–style summary exists in `reports/wrapped_summary.md`
- Behavioral clustering is completed with interpretation OR explicitly skipped with rationale
- The project is reproducible:
  - `README.md` documents setup and execution
  - `requirements.txt` exists

## Out of Scope (v1)
- Full recommender systems (collaborative filtering, neural recommenders)
- Real-time streaming ingestion (Kafka, Spark)
- Production-grade dashboard deployment (auth, CI/CD)
- Multi-user personalization and segmentation at scale
- NLP on lyrics or social data
- Audio signal processing
- Deep model tuning or extensive hyperparameter search

## Phase 1 - Problem Framing

### Problem Statement
- We have listening data available from a user, but we lack understanding of solid trends existing within the data, so it reduces the ability to properly understand a user's full listening habits
### Intended Audience
- Non technical Spotify users who wish to view insights on their listening history in a way that tells a story 

### Key Analytical Questions
- What content dominates my listening?
- When does listening happen?
- Does listening change over days/weeks?
- How intense or passive is listening?
- Are there different modes of listening?


### Assumptions
- This analysis assumes that listening sessions inferred from sequences of plays reasonably represent periods of continuous user engagement.
- This analysis assumes that track- or artist-level genre metadata is a sufficient proxy for representing a user’s musical preferences, despite potential ambiguity or overlap.
- This analysis assumes that longer playback duration generally indicates higher user attention or intent compared to very short or skipped plays.

### Success Criteria
- The analysis produces clear visualizations and summaries that surface temporal and preference-based patterns not immediately obvious from raw listening data.
- A user can identify changes in their listening habits over time through comparative views (e.g., by day, week, or listening period).
- The final outputs present a structured and internally consistent narrative of the user’s listening behavior across artists, genres, and time.

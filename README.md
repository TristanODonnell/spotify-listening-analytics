# Spotify Listening Analytics Project

## Overview
This project analyzes music listening behavior using event-level streaming data.
Inspired by Spotify Wrapped, it transforms raw listening events into behavioral insights.

## Problem Statement
How can user listening patterns and routines be inferred from music streaming data?

## Data

### Source
- Spotify API (track and artist metadata)
- Listening events may be supplemented with synthetic or public data for analysis

User listening data is accessed via Spotify’s Web API with user authorization and is limited to recent playback history. As a result, long-term analyses may rely on accumulated or simulated listening events.

### Schema
- timestamp 
  - Required
  - Raw
  - Datetime
  - The time at which playback of a track began.
- track_id 
  - A unique identifier for the track being played.
  - Required
  - Raw
  - string (ID)

- artist 
  - The primary credited artist associated with the track at the time of playback.
  - Required
  - derived (artist metadata)
  - string

- genre 
  - A categorical label inferred from artist metadata; may be missing or approximate.
  - Required 
  - derived (artist metadata)
  - string (genre label)

- duration_ms 
  - The total duration of the track in milliseconds, not the amount of time listened.
  - Required
  - Raw
  - must be > 0
  - int (milliseconds)

- skipped 
  - A boolean flag indicating whether playback ended before a defined completion threshold.
  - Required
  - derived (from playback duration threshold)
  - Boolean

### Assumptions
- Listening sessions are inferred from timestamp gaps
- Genre labels are derived from artist metadata
- Analysis focuses on a single user

## Methodology
- Data cleaning and feature engineering on event-level listening data
- Exploratory data analysis of temporal, genre, and artist patterns
- Light behavioral clustering to identify listening personas

## Key Insights
- Peak listening times
- Dominant genres and artists
- Identified listening personas

## Outputs
- Jupyter Notebook containing full analysis
- Exported artifacts for quick review:
  - `exports/charts/*.png`
  - `reports/wrapped_summary.md`
  - `data/processed/listening_clean.parquet`
  - (Optional) `exports/wrapped_dashboard.html`

## Tools
- Python
- Pandas, NumPy
- Matplotlib / Seaborn (EDA)
- Plotly (final visualizations)
- Scikit-learn

## Limitations
- Genre labeling ambiguity
- Session inference assumptions
- Single-user scope

## Extensions
- Multi-user comparisons
- Year-over-year analysis
- Recommendation modeling

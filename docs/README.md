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

### Schema
- timestamp
- track_id
- artist
- genre
- duration_ms
- skipped

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

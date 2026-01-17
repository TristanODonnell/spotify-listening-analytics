# config.py

"""
Global configuration for the Spotify / Last.fm listening analytics pipeline.

This file defines:
- Project paths
- Canonical filenames
- Expected schema
- Policy decisions

No data loading or transformation logic belongs here.
"""

from pathlib import Path

# -------------------------------------------------------------------
# Project root & directories
# -------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
CLEANED_DIR = DATA_DIR / "cleaned"

# -------------------------------------------------------------------
# Input / output filenames
# -------------------------------------------------------------------

# Default raw input (Last.fm export for now)
RAW_SCROBBLES_FILENAME = "scrobbles-seekistguy.csv"

# Canonical cleaned dataset output
CLEANED_DATASET_FILENAME = "listening_cleaned.parquet"

# Optional metadata output
RUN_METADATA_FILENAME = "run_metadata.json"

# -------------------------------------------------------------------
# Canonical schema
# -------------------------------------------------------------------

CANONICAL_COLUMNS = [
    "timestamp_utc",
    "timestamp_local"
    "track_id",
    "artist",
    "album",
    "genre",
    "duration_ms",
    "skipped"
]

REQUIRED_COLUMNS = [
    "timestamp_utc",
    "track_id",
    "artist",

]

OPTIONAL_COLUMNS = [
    "genre",
    "album",
    "duration_ms",
    "skipped",
]

# -------------------------------------------------------------------
# Column mapping: raw Last.fm → canonical schema
# (raw column names on the left, canonical names on the right)
# -------------------------------------------------------------------

RAW_TO_CANONICAL_COLUMN_MAP = {
    "track": "track_id",
    "uts": "timestamp_utc",
    "artist": "artist",
    "album": "album",
}

# -------------------------------------------------------------------
# Policy decisions
# -------------------------------------------------------------------

# How to treat missing genres:
# "keep_null" | "label_unknown" | "drop"
MISSING_GENRE_POLICY = "label_unknown"
UNKNOWN_GENRE_LABEL = "Unknown"

# Timestamp handling
# Last.fm timestamps are usually UTC
TIMESTAMP_TIMEZONE = "UTC"

# Skip-related metrics
# Last.fm does not support partial plays
ENABLE_SKIP_METRICS = False
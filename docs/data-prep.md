This phase transforms raw Spotify listening events into an analysis-ready dataset.
The goal of Phase 3 is not to produce insights, but to produce **clean, validated,
and well-defined features** that support downstream analysis and visualization.

All transformations in this phase operate on the canonical `ListeningEvent` schema
and must respect the data-quality rules defined in `data-quality.md`.

---

## Canonical Input Schema

Each input record represents a single listening event with the following fields:

- timestamp
- track_id
- artist
- genre
- duration_ms
- skipped

---

## 1. Convert Timestamps to Temporal Features

### Purpose
Enable time-based analysis of listening behavior by decomposing raw timestamps into
interpretable temporal features such as time of day and day of week.

### Input Fields Required
- timestamp

### Output Fields Produced
- Date-level features (e.g., calendar date)
- Day-level features (e.g., day of week)
- Time-of-day features (e.g., hour)
- Optional higher-level groupings (e.g., weekday vs weekend)

### Key Rules / Assumptions
- All temporal features are derived exclusively from the event timestamp.
- Temporal interpretation is consistent across the dataset (single time standard).
- Derived features do not imply session boundaries or listening intent.

### Edge Cases to Handle
- Missing or null timestamps (record invalid)
- Invalid timestamp formats
- Out-of-range timestamps
- Ambiguous or missing timezone information

---

## 2. Compute Listening-Time Metrics

### Purpose
Define and quantify “listening time” as a measure of user engagement, distinguishing
between total exposure to content and meaningful listening behavior.

### Input Fields Required
- duration_ms
- skipped

### Output Fields Produced
- Per-event listening time attribution
- Aggregated listening-time metrics at various levels (e.g., per day, artist, genre)

### Key Rules / Assumptions
- Track duration represents the maximum possible listening time for an event.
- Skipped events may contribute reduced or zero listening time depending on policy.
- Listening-time metrics must aggregate consistently across dimensions.

### Edge Cases to Handle
- Missing or zero duration values
- Implausibly long durations
- Contradictions between duration and skip status
- Duplicate events inflating listening time

---

## 3. Calculate Skip Rates

### Purpose
Quantify disengagement by measuring how frequently listening events result in skips
relative to total playback events.

### Input Fields Required
- skipped
- track_id (and other grouping dimensions as needed)

### Output Fields Produced
- Skip counts
- Total play counts
- Skip-rate metrics at defined aggregation levels

### Key Rules / Assumptions
- Each listening event represents a single opportunity to skip.
- Skip rate is defined as skipped events divided by total events.
- Skip-rate metrics are only meaningful when play counts exceed a minimum threshold.

### Edge Cases to Handle
- Missing or null skip indicators
- Groups with very low event counts
- Inconsistent skip flags
- Undefined or misleading skip rates due to small denominators

---

## 4. Handle Missing Genres

### Purpose
Ensure genre-based analyses remain interpretable despite incomplete or inconsistent
genre metadata.

### Input Fields Required
- genre

### Output Fields Produced
- Normalized genre field
- Explicit representation for missing or unknown genres

### Key Rules / Assumptions
- Missing genre values are treated as valid but unclassified.
- A consistent policy is applied across all analyses (e.g., “Unknown” bucket or exclusion).
- The chosen policy must be documented due to its impact on genre metrics.

### Edge Cases to Handle
- Null versus empty genre values
- Inconsistent genre naming or casing
- Tracks with ambiguous or broad genre labels
- High proportions of missing genre data skewing results

---

## 5. Produce a Cleaned Dataset

### Purpose
Create a single, analysis-ready dataset that enforces schema consistency, validity,
and documented handling of anomalous records.

### Input Fields Required
- All canonical schema fields
- All derived features from Phase 3 tasks

### Output Fields Produced
- Final cleaned dataset with consistent types and validated values
- Optional indicators for filtered, corrected, or imputed records

### Key Rules / Assumptions
- “Cleaned” means fit for analysis, not necessarily lossless.
- All filtering and normalization decisions follow documented rules.
- The cleaned dataset serves as the sole input for downstream analysis.

### Edge Cases to Handle
- Duplicate listening events
- Records violating multiple quality rules
- Conflicting field values
- Decisions to drop, retain, or flag problematic records

---

## Phase Completion Criteria

Phase 3 is complete when:

- A cleaned listening dataset exists and is saved to disk
- All derived features are documented and reproducible
- Data-quality decisions are explicitly reflected in outputs
- Downstream analysis can proceed without revisiting raw data

At this point, implementation begins.
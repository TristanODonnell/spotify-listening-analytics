# Data Quality Rules - ListeningEvent

## Type Expectations
- timestamp 
  - Expected: datetime (a real timestamp, not free text)

- track_id 
  - Expected: string ID (non-empty)
  
- artist 
  - Expected: string (primary artist name or ID, depending on your choice)

- genre 
  - Expected: string label (derived); may be missing

- duration_ms 
  - Expected: integer (milliseconds)

- skipped 
  - Expected: boolean (true/false)

## Missing-value policy
- timestamp 
  - Missing allowed? No 
  - If missing: record is invalid (cannot place play in time-based analysis)

- track_id 
  - Missing allowed? No 
  - If missing: record is invalid (cannot link to track metadata)

- artist 
  - Missing allowed? No
  - If missing: mark record invalid 

- genre 
  - Missing allowed? Yes 
  - If missing: keep the event, but: group into “Unknown/Unclassified”

- duration_ms 
  - Missing allowed? No 
  - If missing: record is invalid for attention metrics (and likely invalid overall)

- skipped 
  - Missing allowed? No
  - If missing: compute result, most likely would be missing because of other time values missing

## Validity rules

- timestamp must be within the dataset’s overall date range 
- duration_ms must be > 0 and within a reasonable upper bound ( not 0, not 50 hours)
- track_id must be non-empty and stable format (no null/blank)
- skipped must be strictly true/false (no “maybe”)
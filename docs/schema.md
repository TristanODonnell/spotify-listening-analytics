# Schema Documentation v1 

## Overview
This document defines the canonical data schema used for analyzing user listening behavior in the Spotify Listening Analytics project. The schema is designed to support descriptive and exploratory analysis of listening habits, including timing, content preferences, and engagement patterns.

The schema represents listening behavior at the level of individual playback events and is intentionally constrained to fields that can be reliably obtained or derived from Spotify’s Web API and associated metadata.

## Entities

ListeningEvent

A ListeningEvent represents a single instance of a user initiating playback of a track at a specific point in time. Each event captures when playback began, what content was played, and basic indicators of engagement with that content.

ListeningEvents are not sessions and do not imply full track consumption; they represent discrete playback starts that may end early or complete fully.

## Field Dictionary
### timestamp
- Required: Yes 
- Source: Raw 
- Type: Datetime 
- Description: The time at which playback of a track began. This value is used as the primary temporal reference for time-based analyses such as time-of-day, day-of-week, and trend analysis.

### track_id
- Required: Yes 
- Source: Raw 
- Type: String (identifier)
- Description: A unique identifier for the track being played. This field is used to link listening events to track-level metadata such as duration and artist information.

### artist
- Required: Yes 
- Source: Derived (from track metadata)
- Type: String 
- Description: The primary credited artist associated with the track at the time of playback. This field enables artist-level aggregation and preference analysis.

### genre
- Required: No 
- Source: Derived (from artist metadata)
- Type: String 
- Description: A categorical label inferred from artist metadata. Genre values may be missing, approximate, or inconsistent due to limitations in artist-level genre classification.

### duration_ms
- Required: Yes 
- Source: Raw 
- Type: Integer (milliseconds)
- Description: The total duration of the track in milliseconds. This value represents the full length of the track and does not indicate how much of the track was actually listened to.

### skipped
- Required: Yes 
- Source: Derived 
- Type: Boolean 
- Description: A flag indicating whether playback ended before a defined completion threshold. This field is used as a coarse indicator of engagement or passive listening behavior.

## Assumptions and Limitations
- User listening data accessed via Spotify’s Web API is limited to recent playback history and does not represent a complete historical record.
- Genre information is inferred from artist metadata and may be missing, overly broad, or inconsistent across artists.
- A ListeningEvent represents playback initiation and does not guarantee full track consumption. 
- The definition of a “skip” is based on a completion threshold rather than an explicit user action and may be refined in future versions. 
- Long-term trend analysis may rely on accumulated data over time or synthetic listening events for demonstration purposes.

## Example Records

### Example: Typical Listening Event

- timestamp: 2025-01-10T18:42:15Z 
- track_id: 3n3Ppam7vgaVa1iaRUc9Lp 
- artist: Daft Punk 
- genre: Electronic 
- duration_ms: 374000 
- skipped: false

### Example: Edge Case (Missing Genre)
- timestamp: 2025-01-11T09:05:47Z 
- track_id: 6rqhFgbbKwnb9MLmUQDhG6 
- artist: Unknown Artist 
- genre: null 
- duration_ms: 212000 
- skipped: true

In this case, the listening event is valid for time-based and engagement analysis but would be excluded from genre-based breakdowns.
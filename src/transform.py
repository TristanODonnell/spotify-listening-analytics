# transform.py

import pandas as pd
from pandas import DataFrame
from pandas.api.types import (
    is_datetime64_any_dtype,
    is_numeric_dtype,
)

LOCAL_TZ = "America/Los_Angeles"


def _infer_epoch_unit_from_series(s: pd.Series) -> str:
    """
    Infer epoch unit from magnitude.
    - seconds:      ~1e9  (10 digits)  e.g., 1700000000
    - milliseconds: ~1e12 (13 digits)  e.g., 1700000000000
    - microseconds: ~1e15 (16 digits)
    - nanoseconds:  ~1e18 (19 digits)
    """
    # Use median of non-null absolute values for robustness
    non_null = s.dropna()
    if non_null.empty:
        return "s"  # default fallback

    # Work with absolute values (in case of negatives)
    med = float(non_null.abs().median())

    if med >= 1e17:
        return "ns"
    if med >= 1e14:
        return "us"
    if med >= 1e11:
        return "ms"
    return "s"


def transform_timestamp(df: DataFrame) -> DataFrame:
    """
    Ensure df has:
      - timestamp_utc: tz-aware UTC pandas datetime
      - timestamp_local: converted to LOCAL_TZ

    Accepts timestamp_utc as:
      - numeric epoch (seconds/ms/us/ns)
      - ISO datetime strings
      - pandas datetime (tz-aware or tz-naive)
    """
    s = df["timestamp_utc"]

    # Case 1: already datetime-like
    if is_datetime64_any_dtype(s):
        # If tz-naive, assume it's UTC; if tz-aware, normalize to UTC
        if getattr(s.dt, "tz", None) is None:
            df["timestamp_utc"] = s.dt.tz_localize("UTC")
        else:
            df["timestamp_utc"] = s.dt.tz_convert("UTC")

    # Case 2: numeric epoch
    elif is_numeric_dtype(s):
        unit = _infer_epoch_unit_from_series(s)
        df["timestamp_utc"] = pd.to_datetime(s, unit=unit, utc=True, errors="coerce")

    # Case 3: strings / objects (ISO timestamps, etc.)
    else:
        df["timestamp_utc"] = pd.to_datetime(s, utc=True, errors="coerce")

    # Local conversion
    df["timestamp_local"] = df["timestamp_utc"].dt.tz_convert(LOCAL_TZ)

    return df

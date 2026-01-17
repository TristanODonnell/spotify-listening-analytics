# transform.py

import pandas as pd
from pandas import DataFrame

def transform_timestamp(df: DataFrame) -> DataFrame:

    df['timestamp_utc'] = pd.to_datetime(df['timestamp_utc'])

    df["timestamp_utc"] = df["timestamp_utc"].dt.tz_localize("UTC")

    df["timestamp_local"] = df["timestamp_utc"].dt.tz_convert("America/Los_Angeles")

    return df
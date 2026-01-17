# validate.py

from pandas import DataFrame
import src.config as config

def validate_raw(df: DataFrame) -> None:

    if df.empty:
        raise ValueError

    for column in config.REQUIRED_COLUMNS:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    for column in config.REQUIRED_COLUMNS:
        if df[column].isnull().any():
            raise ValueError(f"Required column {column} contains null values")







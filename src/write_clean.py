# write_clean.py

from pandas import DataFrame
import src.config as config



def write_clean(df: DataFrame) -> None:

    config.CLEANED_DIR.mkdir(parents=True, exist_ok=True)

    output_path = config.CLEANED_DIR / config.CLEANED_DATASET_FILENAME

    df.to_parquet(output_path, index=False)


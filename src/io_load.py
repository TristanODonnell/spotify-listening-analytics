# io_load

import pandas as pd
from pandas import DataFrame

import src.config as config


def load_raw_scrobbles() -> DataFrame:
    loaded_raw = pd.read_csv(config.RAW_DIR / config.RAW_SCROBBLES_FILENAME)
    return loaded_raw

def remap_columns(raw: DataFrame) -> DataFrame:
    mapped_scrobbles = raw.rename(columns=config.RAW_TO_CANONICAL_COLUMN_MAP)
    return mapped_scrobbles

if __name__ == "__main__":
    data = load_raw_scrobbles()
    data_mapped = remap_columns(data)
    print(data_mapped.columns)



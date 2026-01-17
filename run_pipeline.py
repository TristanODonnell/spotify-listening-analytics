# run_pipeline.py

from src import config, io_load, transform, validate, write_clean

def run_pipeline():

    raw_df =io_load.load_raw_scrobbles()
    mapped_df = io_load.remap_columns(raw_df)
    validate.validate_raw(mapped_df)
    transformed_df = transform.transform_timestamp(mapped_df)
    write_clean.write_clean(transformed_df)



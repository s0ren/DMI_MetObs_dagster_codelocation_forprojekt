import gzip # see https://docs.python.org/3/library/gzip.html#examples-of-usage
import pandas as pd

def get_jsonl_from_gz(gz_filename: str) -> str:
    with gzip.open(gz_filename, 'rb') as f:
        file_content = f.read()
    return file_content

def process_jsonl_from_gz(gz_filename: str, handler) -> list:
    pass

def jsonl_to_flat_df(jsonl_data: str) -> pd.DataFrame:
    pass

from os.path import basename
import gzip # see https://docs.python.org/3/library/gzip.html#examples-of-usage
import shutil

def get_gzip_out_file_path(src_filepath:str, dst_dir:str='gzip') -> str:
    out_file_name = f"{dst_dir}/{basename(src_filepath)}.gz"
    return out_file_name

def gzip_obs_jsonl(src_filepath:str, dst_dir:str='gzip')-> str:
    out_file_name = get_gzip_out_file_path(src_filepath, dst_dir)
    with open(src_filepath, 'rb') as f_in:
        with gzip.open(out_file_name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return out_file_name
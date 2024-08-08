from datetime import datetime, timedelta
import gzip # see https://docs.python.org/3/library/gzip.html#examples-of-usage

from DMI_MetObs.extraction.dmi_utils import store_data_fs, timestamp10min_aligned, timestamp2filename
import DMI_MetObs.assets.constants as dmi_asset_constants

from DMI_MetObs.transform.compress import (
    get_gzip_out_file_path,
    gzip_obs_jsonl
)

def test_get_gzip_out_file_path():
    #ARRANGE
    fixed_filename = "_data/raw/metops_2024-06-07T00_00_00__02_00.jsonl"
    expected_filename = r"_data/gzip/metops_2024-06-07T00_00_00__02_00.jsonl.gz"
    #ACT
    actual_filename = get_gzip_out_file_path(fixed_filename, dst_dir="_data/gzip")
    #ASSERT
    assert expected_filename == actual_filename


def test_copy_obs_jsonl_to_gzip_fixed_filename():
    #ARRANGE
    fixed_filename = "DMI_MetObs_tests/_data/raw/metops_2024-06-07T00_00_00__02_00.jsonl"
    first_line = rb'{"geometry":{"coordinates":[8.6412,56.93],"type":"Point"},"id":"0006a60c-fd75-7097-1fa0-4aecd03c99cd","type":"Feature","properties":{"created":"2024-06-06T21:59:33.669438Z","observed":"2024-06-06T22:00:00Z","parameterId":"temp_soil_mean_past1h","stationId":"06019","value":14.9}}'
    last_line  = rb'{"geometry":{"coordinates":[10.1353,56.0803],"type":"Point"},"id":"fff8276d-e909-c8fa-f2bb-ff28fe8d80b3","type":"Feature","properties":{"created":"2024-06-06T21:07:02.968369Z","observed":"2024-06-06T21:10:00Z","parameterId":"wind_max","stationId":"06074","value":2.8}}'
    expected_filename = r"DMI_MetObs_tests/_data/gzip/metops_2024-06-07T00_00_00__02_00.jsonl.gz"
    #ACT
    actual_filename = gzip_obs_jsonl(fixed_filename, dst_dir="DMI_MetObs_tests/_data/gzip")
    with open(fixed_filename, 'rb') as f_in:
        orig_firstline = f_in.readline().strip()
        for line in f_in:
            orig_lastline = line.strip()

    with gzip.open(actual_filename, 'rb') as f_out:
        ziped_firstline = f_out.readline().strip()
        for line in f_out:
            ziped_lastline = line.strip()

    #ASSERT
    assert expected_filename == actual_filename
    assert orig_firstline == first_line
    assert ziped_firstline == first_line
    assert orig_firstline == ziped_firstline

    assert orig_lastline == last_line
    assert ziped_lastline == last_line
    assert orig_lastline == ziped_lastline

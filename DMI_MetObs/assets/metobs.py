# from ast import List
from dagster import asset, EnvVar, AssetExecutionContext

import json
import jsonlines
from pydantic import Json
from datetime import datetime, timedelta

# import requests

from DMI_MetObs.extraction.dmi_utils import (
    request_all_features, 
    timestamp_1hour_aligned, 
    timestamp2filename,
    store_data_fs
)
from DMI_MetObs.extraction.metobs import (
    get_obs_hour,
)
from . import constants

from ..partitions import metobs_hourly_partition

@asset
def hourlyObs():
    pass
    

@asset
def latestObservations():
    """Getting the latest wether oberservations from DMI 
    """
    url = "https://dmigw.govcloud.dk/v2/metObs/collections/observation/items"
    
    API_KEY = "b0803242-5b7d-4ac6-93c2-2fb779cba423"
    # API_KEY = EnvVar("DMI_API_KEY")
    timestamp = "2024-06-11T12:10:00Z"
    
    params = {
        "datetime"  : timestamp,
        "api-key"   : API_KEY
    }
    
    features = request_all_features(url, params=params)

    prep_timestamp = timestamp.replace(':', '_')
    
    prep_file_path = constants.METOBS_RAW_TEMPALTE_FILE_PATH.format(prep_timestamp)
    with open(prep_file_path, "w") as outfile:
        json.dump(features, outfile)
    
    prep_file_path = constants.METOBS_RAW_TEMPALTE_FILE_PATH_L.format(prep_timestamp)
    with jsonlines.open(prep_file_path, "w") as writer:
        writer.write_all(features)
    
    return features

@asset(partitions_def=metobs_hourly_partition)
def hourlyObservations(context: AssetExecutionContext):
    API_KEY = "b0803242-5b7d-4ac6-93c2-2fb779cba423"
    partition_date_str = context.partition_key
    partition_date = datetime.strptime(partition_date_str, constants.DATETIME_FORMAT)
    filepath = constants.METOBS_RAW_TEMPALTE_FILE_PATH_L.format(
        timestamp2filename(partition_date)
    )

    obs_features = get_obs_hour(API_KEY, partition_date)
    filesize = store_data_fs(obs_features, filepath)
    # return f"grabbed and storred {filesize} bytes (...plus some linefeeds)"

# @asset
# def plus_two(x :int) -> int:
#     return x+2

@asset
def twentytwo() -> int:
    return 22
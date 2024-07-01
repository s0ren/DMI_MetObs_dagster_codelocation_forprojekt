# from ast import List
from dagster import asset, EnvVar

import json
import jsonlines
from pydantic import Json

# import requests

from DMI_MetObs.extraction.dmi_utils import request_all_features
from . import constants

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

# @asset
# def plus_two(x :int) -> int:
#     return x+2

@asset
def twentytwo() -> int:
    return 22
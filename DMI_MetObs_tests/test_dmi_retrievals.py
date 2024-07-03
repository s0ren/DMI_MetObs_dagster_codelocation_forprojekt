from sqlite3 import Timestamp
import pytest
# from asyncio import constants
# from dagster import (
#     asset,  materialize, load_assets_from_modules, 
#     validate_run_config, 
#     daily_partitioned_config, hourly_partitioned_config,
#     Config, OpExecutionContext,
#     op, job
# )
# from DMI_MetObs.assets.metobs import (
#     latestObservations, 
#     # twentytwo
# )

from DMI_MetObs.extraction.metobs import (
    get_obs_at,
    get_obs_interval,
    get_obs_hour
)

from DMI_MetObs.extraction.dmi_utils import store_data_fs, timestamp10min_aligned, timestamp2filename
import DMI_MetObs.assets.constants as dmi_asset_constants

from datetime import datetime, timedelta


def test_current_obs():
    # Arrange
    API_KEY = "b0803242-5b7d-4ac6-93c2-2fb779cba423"
    
    # timestamp for seneste hele tiende minut
    timestamp = datetime.now().astimezone()
    timestamp = datetime(timestamp.year, timestamp.month, timestamp.day, 
                         timestamp.hour, (timestamp.minute - timestamp.minute % 10), 0).astimezone()
    
    # Act
    data = get_obs_at(API_KEY, timestamp)

    # Assert
    assert len(data) > 0

def test_past_obs():
    # Arrange
    API_KEY = "b0803242-5b7d-4ac6-93c2-2fb779cba423"
    
    timestamp = datetime.fromisoformat("2024-06-11T12:10:00Z")
    
    # Act
    data = get_obs_at(API_KEY, timestamp)

    # Assert
    assert len(data) > 0
    assert len(data) == 990

def test_get_obs_interval_10min():
    # Arrange
    API_KEY = "b0803242-5b7d-4ac6-93c2-2fb779cba423"
    
    from_ts = datetime.fromisoformat("2024-06-11T12:10:00Z")
    to_ts   = from_ts + timedelta(minutes=9)

    # Act
    data = get_obs_interval(API_KEY, from_ts, to_ts)
    first_obs_ts = min(datetime.fromisoformat(f['properties']['observed']) for f in data)
    last_obs_ts  = max(datetime.fromisoformat(f['properties']['observed']) for f in data)

    # Assert
    assert len(data) > 0
    assert len(data) == 990
    assert first_obs_ts == last_obs_ts
    

def test_get_obs_interval_1hour():
    # Arrange
    API_KEY = "b0803242-5b7d-4ac6-93c2-2fb779cba423"
    
    from_ts = datetime.fromisoformat("2024-06-11T12:10:00Z")
    to_ts   = from_ts + timedelta(minutes=59)

    # Act
    data = get_obs_interval(API_KEY, from_ts, to_ts)
    first_obs_ts = min(datetime.fromisoformat(f['properties']['observed']) for f in data)
    last_obs_ts  = max(datetime.fromisoformat(f['properties']['observed']) for f in data)

    # Assert
    assert len(data) > 0
    assert last_obs_ts == first_obs_ts + timedelta(minutes=50)
    assert len(data) == 7254


def test_get_obs_interval_1hour_now():
    # Arrange
    API_KEY = "b0803242-5b7d-4ac6-93c2-2fb779cba423"
    
    # from_ts = datetime.fromisoformat("2024-06-11T12:10:00Z")
    from_ts = timestamp10min_aligned() - timedelta(hours=1)
    to_ts   = from_ts + timedelta(minutes=59)

    # Act
    data = get_obs_interval(API_KEY, from_ts, to_ts)
    first_obs_ts = min(datetime.fromisoformat(f['properties']['observed']) for f in data)
    last_obs_ts  = max(datetime.fromisoformat(f['properties']['observed']) for f in data)

    # Assert
    assert len(data) > 0
    assert last_obs_ts == first_obs_ts + timedelta(minutes=50)
    

def test_get_obs_hour():
    # Arrange
    API_KEY = "b0803242-5b7d-4ac6-93c2-2fb779cba423"
    
    from_ts = datetime.fromisoformat("2024-06-11T12:10:00Z")
    to_ts   = from_ts + timedelta(minutes=60)

    # Act
    data = get_obs_hour(API_KEY, to_ts)
    first_obs_ts = min(datetime.fromisoformat(f['properties']['observed']) for f in data)
    last_obs_ts  = max(datetime.fromisoformat(f['properties']['observed']) for f in data)

    # Assert
    assert len(data) > 0
    assert last_obs_ts == first_obs_ts + timedelta(minutes=50)
    # assert len(data) == 7254


def test_get_obs_hour_now():
    # Arrange
    API_KEY = "b0803242-5b7d-4ac6-93c2-2fb779cba423"
    
    # from_ts = datetime.fromisoformat("2024-06-11T12:10:00Z")
    from_ts = timestamp10min_aligned() - timedelta(hours=1)
    to_ts   = from_ts + timedelta(minutes=59)

    # Act
    data = get_obs_hour(API_KEY, to_ts)
    first_obs_ts = min(datetime.fromisoformat(f['properties']['observed']) for f in data)
    last_obs_ts  = max(datetime.fromisoformat(f['properties']['observed']) for f in data)

    # Assert
    assert len(data) > 0
    assert last_obs_ts == first_obs_ts + timedelta(minutes=50)

def test_store_features_as_jsonl():
    #Arange
    API_KEY = "b0803242-5b7d-4ac6-93c2-2fb779cba423"
    
    timestamp = datetime.fromisoformat("2024-06-11T12:10:00Z")
    filepath = dmi_asset_constants.METOBS_RAW_TEMPALTE_FILE_PATH_L.format(
        timestamp2filename(timestamp)
    )
    data = get_obs_hour(API_KEY, timestamp)
    
    #Act
    expected_filesize = store_data_fs(data, filepath)
    # add number of lines
    expected_filesize += len(data)
    import os
    actual_filesize = os.path.getsize(filepath)

    #Assert
    assert actual_filesize > 0
    assert actual_filesize == expected_filesize
    


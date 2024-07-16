# from dagster import asset, materialize
from fileinput import filename
from DMI_MetObs.extraction.dmi_utils import (
    request_all_features, 
    timestamp10min_aligned, timestamp_1hour_aligned,
    timestamp2filename
)
from datetime import datetime, timedelta

#Pattern:
    #Arrange
    #Act
    #Assert

def test_timestamp10min_aligned_fixed():
    #Arrange
    skewed_timestamp = datetime.fromisoformat("2024-06-11T12:17:21+02:00")
    # timestamp for seneste hele tiende minut
    expected_timestamp = datetime.fromisoformat("2024-06-11T12:10:00+02:00")
    
    #Act
    actual_ts = timestamp10min_aligned(skewed_timestamp)

    #Assert
    assert actual_ts == expected_timestamp

def test_timestamp10min_aligned_fixed_asian_timezone():
    #Arrange
    skewed_timestamp = datetime.fromisoformat("2024-06-11T12:17:21+10:00")
    # timestamp for seneste hele tiende minut
    expected_timestamp = datetime.fromisoformat("2024-06-11T12:10:00+10:00")
    
    #Act
    actual_ts = timestamp10min_aligned(skewed_timestamp)

    #Assert
    assert actual_ts == expected_timestamp

def test_timestamp10min_aligned_fixed_no_timezone():
    #Arrange
    skewed_timestamp = datetime.fromisoformat("2024-06-11T12:17:21")
    # timestamp for seneste hele tiende minut
    expected_timestamp = datetime.fromisoformat("2024-06-11T12:10:00+02:00")
    
    #Act
    actual_ts = timestamp10min_aligned(skewed_timestamp)

    #Assert
    assert actual_ts == expected_timestamp

def test_timestamp10min_aligned_now():
    #Arrange
    # timestamp for seneste hele tiende minut
    expected_timestamp = datetime.now().astimezone()
    expected_timestamp = datetime(expected_timestamp.year, expected_timestamp.month, expected_timestamp.day, 
                         expected_timestamp.hour, (expected_timestamp.minute - expected_timestamp.minute % 10), 0).astimezone()
    #Act
    actual_ts = timestamp10min_aligned()

    #Assert
    assert actual_ts == expected_timestamp


def test_timestamp_1hour_aligned_fixed():
    #Arrange
    skewed_timestamp = datetime.fromisoformat("2024-06-11T12:17:21+02:00")
    # timestamp for seneste hele tiende minut
    expected_timestamp = datetime.fromisoformat("2024-06-11T12:00:00+02:00")
    
    #Act
    actual_ts = timestamp_1hour_aligned(skewed_timestamp)

    #Assert
    assert actual_ts == expected_timestamp

def test_timestamp_1hour_aligned_fixed_asian_timezone():
    #Arrange
    skewed_timestamp = datetime.fromisoformat("2024-06-11T12:17:21+10:00")
    # timestamp for seneste hele tiende minut
    expected_timestamp = datetime.fromisoformat("2024-06-11T12:00:00+10:00")
    
    #Act
    actual_ts = timestamp_1hour_aligned(skewed_timestamp)

    #Assert
    assert actual_ts == expected_timestamp

def test_timestamp_1hour_aligned_fixed_no_timezone():
    #Arrange
    skewed_timestamp = datetime.fromisoformat("2024-06-11T12:17:21")
    # timestamp for seneste hele tiende minut
    expected_timestamp = datetime.fromisoformat("2024-06-11T12:00:00+02:00")
    
    #Act
    actual_ts = timestamp_1hour_aligned(skewed_timestamp)

    #Assert
    assert actual_ts == expected_timestamp

def test_timestamp_1hour_aligned_now():
    #Arrange
    # timestamp for seneste hele tiende minut
    expected_timestamp = datetime.now().astimezone()
    expected_timestamp = datetime(expected_timestamp.year, expected_timestamp.month, expected_timestamp.day, 
                         expected_timestamp.hour, 0, 0).astimezone()
    #Act
    actual_ts = timestamp_1hour_aligned()

    #Assert
    assert actual_ts == expected_timestamp


def test_request_all_pages_limit500():
    # Arrange
    url = "https://dmigw.govcloud.dk/v2/metObs/collections/observation/items"
    API_KEY = "b0803242-5b7d-4ac6-93c2-2fb779cba423"
    timestamp = "2024-06-11T12:10:00Z"
    params = {
        "datetime"  : timestamp,
        "api-key"   : API_KEY,
        "limit"     : 500,
    }

    # Act
    data = request_all_features(url, params=params)

    # Assert
    assert len(data) == 990

def test_request_all_pages():
    # Arrange
    url = "https://dmigw.govcloud.dk/v2/metObs/collections/observation/items"
    API_KEY = "b0803242-5b7d-4ac6-93c2-2fb779cba423"
    timestamp = "2024-06-11T12:10:00Z"
    params = {
        "datetime"  : timestamp,
        "api-key"   : API_KEY,
    }

    # Act
    data = request_all_features(url, params=params)

    # Assert
    assert len(data) == 990

def test_timestamp2filename():
    #Arrange
    timestamp = datetime.fromisoformat("2024-06-11T12:10:00Z")
    expected_filename = "2024-06-11T14_10_00__02_00"

    #Act
    filename = timestamp2filename(timestamp)

    #Assert
    assert filename == expected_filename

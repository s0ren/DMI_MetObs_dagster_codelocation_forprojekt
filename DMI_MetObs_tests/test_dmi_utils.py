# from dagster import asset, materialize
from DMI_MetObs.dmi_utils import request_all_features


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
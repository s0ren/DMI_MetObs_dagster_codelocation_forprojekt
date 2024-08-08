import json
import pydantic
import requests
from pydantic import Json, AwareDatetime
import jsonlines
from datetime import datetime, timedelta

from DMI_MetObs.assets import constants

def timestamp10min_aligned(timestamp : datetime = datetime.now().astimezone() ) -> AwareDatetime:
    """_summary_
    Aligns a datetime to nearest previus whole 10 minutes, timezone aware. Defaults to now.
    This conforms to DMI Observations api.

    Args:
        timestamp (datetime, optional): The timestamp to align. Defaults to datetime.now().astimezone().

    Returns:
        AwareDatetime: The datetime aligned to nearest whole ten minutes. Allways going back to previus ten minute tick mark.
        The returned timestamp is allways timezoneaware, if the input is not,the timezone will be the local timezone.
    """
    # timestamp for seneste hele tiende minut
    return datetime(timestamp.year, timestamp.month, timestamp.day, 
                         timestamp.hour, (timestamp.minute - timestamp.minute % 10), 0, tzinfo=timestamp.tzinfo).astimezone()
    
def timestamp_1hour_aligned(timestamp : datetime = datetime.now().astimezone() ) -> AwareDatetime:
    """Aligns datetime to nearest previus whole hour, timezone aware. 
    Defaults to now.

    Args:
        timestamp (datetime, optional): The timestamp to align. Defaults to datetime.now().astimezone().

    Returns:
        AwareDatetime: The datetime aligned to nearest whole hour. Allways going back to previus whole hour tick mark.
        The returned timestamp is allways timezoneaware, if the input is not, the timezone will be the local timezone.
    """
    return datetime(timestamp.year, timestamp.month, timestamp.day, 
                         timestamp.hour, 0, 0, tzinfo=timestamp.tzinfo).astimezone()

def request_all_features(url :str, params :dict) -> list[Json]:
    obs = []
    res = requests.get(url, params=params)
    next_link = ""
    while res.status_code == 200 and next_link is not None:
        json = res.json()
        obs += json['features']
        next_link = next(( lnk['href'] for lnk in json['links'] if lnk['rel'] == 'next'), None)
        if next_link:
            res = requests.get(next_link)
    return obs

def store_data_fs(data: str, filepath: str):
    with jsonlines.open(filepath, "w", compact=True) as writer:
        numWritten = writer.write_all(data)
    return numWritten

def timestamp2filename(timestamp: AwareDatetime) -> str:
    # filepath = timestamp.astimezone().isoformat().replace(':', '_').replace('+','__')
    filepath = timestamp.strftime(constants.DATETIME_FORMAT)
    return filepath
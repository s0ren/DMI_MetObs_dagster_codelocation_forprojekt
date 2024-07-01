import json
import pydantic
import requests
from pydantic import Json, AwareDatetime

from datetime import datetime, timedelta

def timestamp10min_aligned(timestamp : datetime = datetime.now().astimezone() ) -> AwareDatetime:
    """_summary_
    Alligns a datetime to nearest previus whole 10 minutes, timezoneaware. Defaults to now.
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

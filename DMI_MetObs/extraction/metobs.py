"""_summary_
Forretningslogik for at hente meteologiske observationer fra DMI
Jeg vil gerne kunne hente _det hele_!
"""

from datetime import datetime, timedelta
from .dmi_utils import request_all_features, timestamp10min_aligned

from pydantic import (
    AwareDatetime,
    Json
)

def get_obs_at(API_KEY :str, timestamp: AwareDatetime = datetime.now() ) -> list[Json]:
    """ Get observation from the the timestamp specified. Now if not specified.

    Args:
        API_KEY (str): Valid API_KEY for DMI_obs
        timestamp (AwareDatetime, optional): _description_. Defaults to datetime.now().

    Returns:
        list[Json]: _description_
    """
    url = "https://dmigw.govcloud.dk/v2/metObs/collections/observation/items"
    params = {
        "datetime"  : timestamp10min_aligned(timestamp).astimezone().isoformat(),
        "api-key"   : API_KEY
    }
    features = request_all_features(url, params=params)
    return features

def get_obs_interval(API_KEY :str, timestamp_from :AwareDatetime, timestamp_to :AwareDatetime ) -> list[Json]:
    """ Get all observationes within interval between timestamp_from until timestamp_to
    [FIXME] Both inclusive?

    Args:
        API_KEY (str): Valid API_KEY for DMI_obs
        timestamp_from (AwareDatetime): from time
        timestamp_to (AwareDatetime): to time

    Returns:
         list[Json]: retrieved features from interval
    """
    url = "https://dmigw.govcloud.dk/v2/metObs/collections/observation/items"
    params = {
        "datetime"  : timestamp10min_aligned(timestamp_from).astimezone().isoformat()
                      + "/" + timestamp10min_aligned(timestamp_to).astimezone().isoformat(),
        "api-key"   : API_KEY
    }
    features = request_all_features(url, params=params)
    return features

def get_obs_hour(API_KEY :str, timestamp_to :AwareDatetime) -> list[Json]:
    """
    Get all observation from timestamp_from and one hour back.
    Calls get_obs_interval()
    
    Args:
        API_KEY (str): Valid API_KEY for DMI_obs
        timestamp_to (AwareDatetime): to time

    Returns:
        list[Json]: retrieved features from datetime_from and one hour back
    """
    timestamp_from = timestamp_to - timedelta(hours=1)
    return get_obs_interval(API_KEY, timestamp_from, timestamp_to)

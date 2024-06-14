import json
import requests

def request_all_features(url :str, params :dict) -> list:
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

import os
WORKSPACE_ROOT = os.path.abspath(os.path.dirname(__file__) + '/..')
print(WORKSPACE_ROOT)
DATA_ROOT = "data"
METOBS_RAW_TEMPALTE_FILE_PATH = DATA_ROOT + "/raw/metops_{}.json"
METOBS_RAW_TEMPALTE_FILE_PATH_L = DATA_ROOT + "/raw/metops_{}.jsonl"

STARTDATE = "2024-06-01"
STARTDATETIME = STARTDATE + "T12:00:00+0200"

DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S%z" # or just iso, but timezones an milisoconds ... Ohno
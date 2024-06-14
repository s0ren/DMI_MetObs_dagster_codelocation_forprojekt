import os
WORKSPACE_ROOT = os.path.abspath(os.path.dirname(__file__) + '/..')
print(WORKSPACE_ROOT)
DATA_ROOT = "data"
METOBS_RAW_TEMPALTE_FILE_PATH = DATA_ROOT + "/raw/metops_{}.json"
METOBS_RAW_TEMPALTE_FILE_PATH_L = DATA_ROOT + "/raw/metops_{}.jsonl"

metobs_realtime_startdate = "2024-06-01"

DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d" # or just iso, but timezones an milisoconds ... Ohno
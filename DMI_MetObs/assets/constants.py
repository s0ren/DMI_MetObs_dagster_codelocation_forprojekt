import os
WORKSPACE_ROOT = os.path.abspath(os.path.dirname(__file__) + '/..')
# print(WORKSPACE_ROOT)
DATA_ROOT = "data"
METOBS_RAW_TEMPALTE_FILE_PATH = DATA_ROOT + "/raw/metops_{}.json"
METOBS_RAW_TEMPALTE_FILE_PATH_L = DATA_ROOT + "/raw/metops_{}.jsonl"

STARTDATE = "2024-10-30"
STARTDATETIME = STARTDATE + "T00.00.00+0200"

DATE_FORMAT = "%Y-%m-%d"
# DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S%z" # or just iso, but timezones an milisoconds ... Ohno
DATETIME_FORMAT = "%Y-%m-%dT%H.%M.%S%z" # NOT ISO, since dagster uses this for patitionkeys, 
                                        # and stores a file with partitionstate, 
                                        # using the key as filename, and iso datetime contains caracters
                                        # illegal in filenames (':', '+').
                                        # Perhaps this behavior can be configured, but for now i don't know how.
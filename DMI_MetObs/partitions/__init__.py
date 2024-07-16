from dagster import TimeWindowPartitionsDefinition, HourlyPartitionsDefinition
from ..assets import constants

start_date = constants.STARTDATE
start_datetime = constants.STARTDATETIME

# metobs_realtime_partition = TimeWindowPartitionsDefinition(
#     fmt=constants.DATETIME_FORMAT,
#     cron_schedule="*/10 * * * *",
#     start=start_datetime
# )

metobs_hourly_partition = HourlyPartitionsDefinition(
    start_date=start_datetime,
    minute_offset=0,
    timezone="Europe/Copenhagen",
    # fmt="%Y-%m-%dT%H:%M:%S%z",
    fmt=constants.DATETIME_FORMAT,
)
# man kunne teste denne som i DMI_MetObs_tests\test_fra_tutorial.py, 
# eller sige at den er testet der
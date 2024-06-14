from dagster import TimeWindowPartitionsDefinition
from ..assets import constants

start_date = constants.START_DATE

metobs_realtime_partition = TimeWindowPartitionsDefinition(
    cron_expression="10/ * * * *",
    start_date=start_date
)
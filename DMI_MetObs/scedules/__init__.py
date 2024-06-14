from dagster import ScheduleDefinition
from ..jobs import metobs_realtime_update_job, trip_update_job, weekly_update_job

metobs_update_schedule = ScheduleDefinition(
    job=metobs_realtime_update_job,
    cron_schedule="10/ * * * *", # every 5th of the month at midnight
)
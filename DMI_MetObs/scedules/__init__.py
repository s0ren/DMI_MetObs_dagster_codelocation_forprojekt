from dagster import ScheduleDefinition
from ..jobs import metobs_realtime_update_job

metobs_update_schedule = ScheduleDefinition(
    job=metobs_realtime_update_job,
    # cron_schedule="10/ * * * *", # every 10 minutes
    cron_schedule="0 * * * * *", # at 0 minute, every hour, day-of-month, month, week-day, year
)
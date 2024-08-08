from dagster import ScheduleDefinition, build_schedule_from_partitioned_job
from ..jobs import metobs_hourly_update_job # metobs_realtime_update_job

metobs_update_schedule = ScheduleDefinition(
    job=metobs_hourly_update_job,
    # cron_schedule="10/ * * * *", # every 10 minutes
    cron_schedule="0 * * * *", # at 0 minute, every hour, day-of-month, month, week-day, year
)

metobs_update_schedule2 = build_schedule_from_partitioned_job(metobs_hourly_update_job)
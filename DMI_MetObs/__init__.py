from dagster import Definitions, load_assets_from_modules

#import imp

from .assets import metobs # ,OtherDataObs 
from .resources import database_resource
# from .jobs import trip_update_job, weekly_update_job, adhoc_request_job
from .jobs import metobs_hourly_update_job
# from .schedules import trip_update_schedule, weekly_update_schedule
from .scedules import metobs_update_schedule, metobs_update_schedule2
# from .sensors import adhoc_request_sensor

metobs_assets = load_assets_from_modules([metobs])

all_jobs = [metobs_hourly_update_job] #[trip_update_job, weekly_update_job, adhoc_request_job]
all_schedules = [metobs_update_schedule2] # [trip_update_schedule, weekly_update_schedule]
all_sensors = [] # [adhoc_request_sensor]

defs = Definitions(
    assets=[*metobs_assets],
    resources={
        "database": database_resource,
    },
    jobs=all_jobs,
    schedules=all_schedules,
    sensors=all_sensors
)

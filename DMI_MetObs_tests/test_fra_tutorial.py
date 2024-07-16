# from asyncio import constants
import pytest
from dagster import (
    validate_run_config, 
    hourly_partitioned_config,
    Config, OpExecutionContext,
    op, job
    # asset,  materialize, load_assets_from_modules, 
    # daily_partitioned_config, 
)
# from DMI_MetObs.assets.metobs import latestObservations, twentytwo
# from DMI_MetObs.jobs import metobs_realtime_update_job

from datetime import datetime, timedelta

import DMI_MetObs.assets.constants as dmi_asset_constants

###############
# inspireret af https://docs.dagster.io/concepts/partitions-schedules-sensors/testing-partitions#testing-partitioned-config
#
# Se også:
#  - https://docs.dagster.io/guides/dagster/testing-assets#testing-an-individual-asset
#  - https://docs.dagster.io/concepts/testing
#
# Dagster Docs:
#  - https://docs.dagster.io/_apidocs/partitions#
#
###############

@hourly_partitioned_config(
        # start_date=datetime.fromisoformat(dmi_asset_constants.STARTDATETIME),
        start_date=datetime.strptime(dmi_asset_constants.STARTDATETIME, dmi_asset_constants.DATETIME_FORMAT),
        timezone="Europe/Copenhagen",
        fmt="%Y-%m-%dT%H.%M.%S%z")
def my_partitioned_config(start: datetime, end: datetime):
    return {
        "ops": {
            # "process_data_for_datetime": {"config": {"date": start.strftime("%Y-%m-%d")}}
            # "process_data_for_datetime": {
            "process_data": {
                "config": {
                    # "date"  : start.strftime(dmi_asset_constants.DATETIME_FORMAT),
                    "start" : start.strftime(dmi_asset_constants.DATETIME_FORMAT),
                    "end"   : end.strftime(dmi_asset_constants.DATETIME_FORMAT),
                }
            }
        }
    }

class ProcessDataConfig(Config):
    start: str
    end: str


@op
def process_data(context: OpExecutionContext, config: ProcessDataConfig):
    s = config.start
    e = config.end
    context.log.info(f"processing data for {s} - {e}")


@job(config=my_partitioned_config)
def do_more_stuff_partitioned():
    process_data()

@pytest.mark.filterwarnings("ignore:DeprecationWarning:")
def test_my_partitioned_config():
    # assert that the decorated function returns the expected output
    run_config = my_partitioned_config(datetime(2024, 6, 1), datetime(2024, 6, 2))
    assert run_config == {
        "ops": {
            # "process_data_for_datetime": {
            "process_data": {
                "config": {
                    "start": "2024-06-01T00.00.00",
                    "end"  : "2024-06-02T00.00.00"
                }
            }
        }
    }
    # assert that the output of the decorated function is valid configuration for the
    # partitioned_op_job job
    assert validate_run_config(do_more_stuff_partitioned, run_config)


def test_today_num_hours_from_midnight():
    dt = datetime.now()
    # sd = datetime.fromisoformat(dmi_asset_constants.STARTDATETIME)
    sd = datetime.strptime(dmi_asset_constants.STARTDATETIME, dmi_asset_constants.DATETIME_FORMAT)
    # assert sd == 0
    # assert datetime.now().astimezone().isoformat(timespec='minutes') == ""
    # assert dt.isoformat() == ""
    # assert dt.hour == 22
    midnight = datetime(dt.year, dt.month, dt.day, 0, 0, 0)
    dd = dt - midnight
    # assert dd != 0
    assert dd.seconds//3600 == dt.hour
    # hours_from_startdate = (datetime.now().astimezone() - datetime.fromisoformat(dmi_asset_constants.STARTDATETIME)).total_seconds() // 3600
    hours_from_startdate = (datetime.now().astimezone() 
                                - datetime.strptime(
                                    dmi_asset_constants.STARTDATETIME,
                                    dmi_asset_constants.DATETIME_FORMAT
                                )
                            ).total_seconds() // 3600
    # assert hours_from_startdate == 369

@pytest.mark.filterwarnings("ignore:DeprecationWarning:")
def test_my_partitioned_config_keys():
    # Arrange
    startdatetime = datetime.strptime(dmi_asset_constants.STARTDATETIME, dmi_asset_constants.DATETIME_FORMAT)
    hours_from_startdate = (
        datetime.now().astimezone() - startdatetime
    ).total_seconds() // 3600
    # test that the partition keys are what you expect
    run_config = my_partitioned_config(
        startdatetime, 
        startdatetime + timedelta(days=1)
    )
    # Act
    keys = my_partitioned_config.get_partition_keys()
    # Assert
    assert keys[0] == "2024-06-01T12.00.00+0200"
    assert keys[1] == "2024-06-01T13.00.00+0200"
    #assert keys[-1] == "2024-06-01-23:00"
    assert len(keys) == hours_from_startdate
    # test that the run_config for a partition is valid for partitioned_op_job
    run_config = my_partitioned_config.get_run_config_for_partition_key(keys[0])
    assert validate_run_config(do_more_stuff_partitioned, run_config)
    # test that the contents of run_config are what you expect
    assert run_config == {
        "ops": {
            "process_data": {
                "config": {"start": "2024-06-01T12.00.00+0200", "end": "2024-06-01T13.00.00+0200"}
            }
        }
    }
    # an hour later
    # test that the run_config for a partition is valid for partitioned_op_job
    run_config = my_partitioned_config.get_run_config_for_partition_key(keys[1])
    assert validate_run_config(do_more_stuff_partitioned, run_config)
    # test that the contents of run_config are what you expect
    assert run_config == {
        "ops": {
            "process_data": {
                "config": {"start": "2024-06-01T13.00.00+0200", 
                            "end":  "2024-06-01T14.00.00+0200"}
            }
        }
    }

def test_partitioned_op_job():
    assert do_more_stuff_partitioned.partitioned_config.get_partition_keys()[0] == dmi_asset_constants.STARTDATETIME
    assert do_more_stuff_partitioned.execute_in_process(
    #    partition_key=datetime.fromisoformat(dmi_asset_constants.STARTDATETIME).isoformat()
        partition_key=dmi_asset_constants.STARTDATETIME
    ).success

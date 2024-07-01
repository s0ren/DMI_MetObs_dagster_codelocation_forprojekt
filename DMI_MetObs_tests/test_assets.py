"""
    I høj grad afluret fra https://docs.dagster.io/concepts/partitions-schedules-sensors/testing-partitions
"""

# from asyncio import constants
import pytest
# from asyncio import constants
# from dagster import (
#     asset,  materialize, load_assets_from_modules, 
#     validate_run_config, 
#     daily_partitioned_config, hourly_partitioned_config,
#     Config, OpExecutionContext,
#     op, job
# )
from DMI_MetObs.assets.metobs import (
    latestObservations, 
    # twentytwo
)
from DMI_MetObs.jobs import metobs_realtime_update_job

# from dagster import validate_run_config, daily_partitioned_config, hourly_partitioned_config
from datetime import datetime, timedelta

import DMI_MetObs.assets.constants as dmi_asset_constants


def _test_oneObs_asset():
    # Arrange
    #assets = [metObs]

    # Act
    #result = materialize(assets)
    obs = latestObservations()

    # Assert
    assert obs is not None
    #assert len(res['features']) == 990
    assert len(obs) > 0

def _test_oneHour_ObsservationAsset():
    # Arrange
    # setup config w start:datatime

    # Act
    # fetch

    # Assert
    # So many observations
    pass

# def _test_plustwo():
#     # Arrange
#     # Act
#     # Assert
#     assert plus_two(2) == 4

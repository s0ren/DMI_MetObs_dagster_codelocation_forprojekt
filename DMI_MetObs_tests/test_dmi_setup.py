import pytest

# from DMI_MetObs.extraction.dmi_utils import store_data_fs, timestamp10min_aligned, timestamp2filename
import DMI_MetObs.assets.constants as dmi_asset_constants

from DMI_MetObs.extraction.dmi_utils import timestamp_1hour_aligned
from DMI_MetObs.partitions import metobs_hourly_partition

from datetime import datetime, timedelta

def test_metobs_hourly_partition():
    #ARRANGE
    expected_start = datetime.strptime(dmi_asset_constants.STARTDATETIME, dmi_asset_constants.DATETIME_FORMAT) 
    expected_start_str = expected_start.strftime(dmi_asset_constants.DATETIME_FORMAT)
    # expected_end = datetime.now().astimezone()
    expected_end = timestamp_1hour_aligned() - timedelta(hours=1)
    expected_end_str = expected_end.strftime(dmi_asset_constants.DATETIME_FORMAT)
    #ACT
    first = metobs_hourly_partition.get_first_partition_key()
    last = metobs_hourly_partition.get_last_partition_key()
    #ASSERT
    assert metobs_hourly_partition.start == expected_start
    assert metobs_hourly_partition.end == None
    assert metobs_hourly_partition.timezone == "Europe/Copenhagen"
    assert metobs_hourly_partition.fmt == dmi_asset_constants.DATETIME_FORMAT

    assert first == expected_start_str
    assert last == expected_end_str


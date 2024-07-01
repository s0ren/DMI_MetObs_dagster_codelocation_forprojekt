from dagster import AssetSelection, define_asset_job
from ..partitions import metobs_realtime_partition, metobs_hourly_partition

metobs_realtime = AssetSelection.assets("latestObservations")

metobs_realtime_update_job = define_asset_job(
    name="metobs_realtime_update_job",
    selection=metobs_realtime,
    #partitions_def=metobs_realtime_partition,
    partitions_def=metobs_hourly_partition,
)

from dagster import asset, materialize, load_assets_from_modules
from DMI_MetObs.assets.metobs import latestObservations, twentytwo

def test_oneObs_asset():
    # Arrange
    #assets = [metObs]

    # Act
    #result = materialize(assets)
    obs = latestObservations()

    # Assert
    assert obs is not None
    #assert len(res['features']) == 990
    assert len(obs) > 0

# def _test_plustwo():
#     # Arrange
#     # Act
#     # Assert
#     assert plus_two(2) == 4

def _test_twentytwo():
    # Arrange
    # Act
    # Assert
    assert twentytwo() == 22


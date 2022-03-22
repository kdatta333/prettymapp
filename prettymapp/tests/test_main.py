import pytest
from geopandas import GeoDataFrame
from shapely.geometry import box
from pyproj import CRS

from prettymapp.main import get_osm_geometries
from prettymapp.plotting import Plot
from prettymapp.settings import STYLES

AOI = box(
    13.373621926483281, 52.507705884952586, 13.374621926483281, 52.508705884952586
)
AOI_UTM_CRS = CRS.from_user_input(32632)


@pytest.mark.live
def test_get_geometries_live():
    df = get_osm_geometries(AOI, AOI_UTM_CRS)
    assert isinstance(df, GeoDataFrame)
    assert not df.empty


@pytest.mark.live
def test_main_live():
    df = get_osm_geometries(AOI, AOI_UTM_CRS)
    fig = Plot(df=df, aoi_bounds=AOI.bounds, draw_settings=STYLES["Peach"]).plot_all()
    assert fig is not None
    # assert isinstance(fig, int)
    # import matplotlib.pyplot as plt
    # plt.show()

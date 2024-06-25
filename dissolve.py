# Import modules
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import pyogrio
import time
import numpy as np
from shapely.geometry import MultiPolygon
from multiprocessing import Pool
from functools import partial
from osgeo import ogr, gdal
# gpd.options.io_engine = "pyogrio"
pd.set_option('display.max_columns',None)
from tqdm import tqdm
import pickle as pkl
from concurrent.futures import ThreadPoolExecutor, as_completed
import geofileops as gfo
# Load the data from the shapefiles
# Load basins
H8=gpd.read_file("World/Basins/basins_continents_countries.shp", engine="pyogrio")
main_bas_counts = H8['MAIN_BAS'].value_counts()
#load PAs (Protected Areas)
PAs=gpd.read_file("World/PAs/Merged_PAs.shp", engine="pyogrio")
PAs = PAs
# Check and filter out invalid geometries
valid_geom_mask = PAs.geometry.is_valid
PAs_valid = PAs[valid_geom_mask]
print("c")
PAs_valid = PAs_valid[['PA_DEF','geometry']]
# Dissolve based on the chosen field to unify all PAs in one feature
gfo.to_file(PAs_valid, ".cache/PAs_valid.gpkg")
gfo.dissolve(
    input_path=".cache/PAs_valid.gpkg",
    output_path=".cache/dissolve_output.gpkg",
    explodecollections=False,
    groupby_columns=["PA_DEF"],
)
PA_dis = gpd.read_file(".cache/dissolve_output.gpkg")
PAs_dis["PROTECTED"]=1
# be careful running this
with open(".cache/world_data_PARTIAL_gfo.pkl", "wb") as f:
    pkl.dump([H8, main_bas_counts,PAs, valid_geom_mask,PAs_valid,PAs_dis], f)

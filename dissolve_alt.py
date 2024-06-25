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
# gpd.options.io_engine = "pyogrio"
pd.set_option('display.max_columns',None)
from tqdm import tqdm
import pickle as pkl
from concurrent.futures import ThreadPoolExecutor, as_completed
from osgeo import ogr, gdal
import geofileops as gfo
with open(".cache/PAs_valid.pkl", "rb") as f:
    PAs_valid = pd.read_pickle(f)
with open(".cache/PAs_dis.pkl","rb") as f:
    PAs_dis = pd.read_pickle(f)
print(PAs_dis)
#PAs_valid.drop([138770,138771,138772,138773,138774,138775])
print("length of PAs_valid:")
print(PAs_valid.shape[0])
print("Starting dissolve.")
gfo.to_file(PAs_valid, ".cache/PAs_valid.gpkg")
gfo.dissolve(
    input_path=".cache/PAs_valid.gpkg",
    output_path=".cache/dissolve_output.gpkg",
    explodecollections=False,
)
PAs_dis = gpd.read_file(".cache/dissolve_output.gpkg")
PAs_dis["PROTECTED"]=1
with open(".cache/PAs_dis_all.pkl","wb") as f:
    pkl.dump(PAs_dis,f)
print("Finished dissolve_alt.")

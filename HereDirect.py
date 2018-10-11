import os
import sys
import numpy as np
import pandas as pd
import requests
from shapely.geometry import Point, Polygon, LineString, LinearRing

#### CREDENTIALS ####

credentials = np.load(r"C:\Skyhook\HERE\HERE_API_credentials.npy")

# apiID = 'vQUXblWlsSzsBSJNRDax'
# apiCode = 'f4f3xSQqZX5l3m6ur86jAQ'

appID = credentials[1]
appCode = credentials[2]



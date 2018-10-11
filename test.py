import numpy as np
import pandas as pd
import time
import herepy
from pandasql import sqldf


credentials = np.load(r"C:\Skyhook\HERE\HERE_API_credentials.npy")

# apiID = 'vQUXblWlsSzsBSJNRDax'
# apiCode = 'f4f3xSQqZX5l3m6ur86jAQ'

appID = credentials[1]
appCode = credentials[2]



placesApi = herepy.PlacesApi(appID, appCode)
lat, lng = map(float, location.strip('()').split(','))

nearbyResponse = placesApi.nearby_places([lat, lng])
try:
    data = nearbyResponse.as_dict()
    print(data)
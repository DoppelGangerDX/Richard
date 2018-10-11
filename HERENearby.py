
import sys
import numpy as np
import pandas as pd
import time
import herepy
from pandasql import sqldf
from pprint import pprint
from collections import abc
import datetime
#### USER INPUTS #####

# fpath = sys.argv[1]
# column_name = sys.argv[2]

#fpathNearby = "C:/Skyhook/HERE/POI_Seedpoints.xlsx"
fpathNearby = "C:/temp/R/POI_Seedpoints.xlsx"

nearbyPlaces_path = "C:/temp/R/NearbyOutput.xlsx"
#nearbyPlaces_path = "C:/Skyhook/HERE/NearbyOutput.xlsx"


#credentials = np.load("C:\Skyhook\HERE\HERE_API_credentials.npy")
credentials = np.load("C:/temp/R/HERE_API_credentials.npy")


appID = credentials[1]
appCode = credentials[2]



def nearbyPlaces_dataset(fpathNearby, column_name):

    try:
        excel = pd.read_excel(fpathNearby)

    except:

        try:
            excel = pd.read_csv(fpathNearby)

        except:
            "Input File Read Error!! Please check Format."

    for t in range(len(excel)):


        location= excel.loc[t, column_name]
        placesApi = herepy.PlacesApi(appID, appCode)
        lat, lng = map(float, location.strip('()').split(','))

        nearbyResponse = placesApi.places_with_language([lat, lng], 'ar')

        # try:

        data = nearbyResponse.as_dict()
        for i in range(0, (len(data['results']['items']))):
            title = 'title' + str(i)
            distance = 'distance' + str(i)
            position = 'position' + str(i)
            category = 'category' + str(i)

            excel.loc[t,title] = str(data['results']['items'][i]['title'])
            excel.loc[t, distance] =str(data['results']['items'][i]['distance'])
            excel.loc[t, position] = str(data['results']['items'][i]['position'])
            excel.loc[t, category] = str(data['results']['items'][i]['category']['title'])
            time.sleep(0.1)

    return excel



nearbyPlaces_output = nearbyPlaces_dataset(fpathNearby, 'Origin')
nearbyPlaces_output.to_excel(nearbyPlaces_path)

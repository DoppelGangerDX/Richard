import geohash2
import sys
import numpy as np
import pandas as pd
from pathlib import Path



directory_in_str=r'C:\Skyhook\sgwm2\out2\skWithCoord'
pathlist = Path(directory_in_str).glob('**/*.csv')
i= 1
for path in pathlist:
    path_in_str = str(path)
    print(path_in_str)
    out= r'\Out'+ str(i)
    fpath = path_in_str
    Output_path = directory_in_str+ out+ ".xlsx"
    print(Output_path)

    i=i+1

    def Geohash(fpath, column_name1, column_name2):
        try:
            data = pd.read_csv(fpath)

        except:

            try:
                data = pd.read_csv(fpath)

            except:
                "Input File Read Error!! Please check Format."

        for i in range(len(data)):
            lat = float(data.loc[i, column_name1])
            lon = float(data.loc[i, column_name2])
            #print(lat,lon)
            geohash=geohash2.encode(lat, lon, precision=9)
            #print(geohash)
            data.loc[i, 'Geohash'] = geohash

        return data
    output = Geohash(fpath, 'Lat', 'Lon')
    output.to_excel(Output_path)

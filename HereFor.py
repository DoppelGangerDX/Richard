
import numpy as np
import pandas as pd
import time
import herepy
from pathlib import Path


directory_in_str=r'C:\Skyhook\HERE\Uk\Time Series\oldham'
pathlist = Path(directory_in_str).glob('**/*.xlsx')
i= 1
for path in pathlist:

    path_in_str = str(path)
    print(path_in_str)
    out= r'\Out'+ str(i)

    fpath = path_in_str

    carOutput_path = directory_in_str+ out+ ".xlsx"

    totalOutput_path = directory_in_str+ out+ ".xlsx"

    print(carOutput_path)
    data = pd.read_excel(fpath)
    i=i+1

    credentials = np.load(r"C:\Skyhook\HERE\HERE_API_credentials.npy")
    appID = credentials[1]
    appCode = credentials[2]




    def totalRouting_dataset(fpath, column_name1, column_name2  ):
        try:
            data = pd.read_excel(fpath)

        except:

            try:
                data = pd.read_csv(fpath)

            except:
                "Input File Read Error!! Please check Format."


        for i in range(len(data)):

            for t in range(00,24):
                try:
                    title = 'Car' + str(t)

                    if t < 10:
                        hour=t
                        flag =1
                    if t >=10 and t < 24:
                        hour= t
                        flag = 0
                    if t == 24:
                        hour = 00
                        flag = 0
                    #print(hour)
                    routingApi = herepy.RoutingApi(appID, appCode)
                    ProutingApi = herepy.RoutingApi(appID, appCode)

                    location1 = data.loc[i, column_name1]
                    location2 = data.loc[i, column_name2]

                    lat, lng = map(float, location1.strip('()').split(','))
                    lat2, lng2 = map(float, location2.strip('()').split(','))

                    if flag == 1:
                        getRoutingData = routingApi.car_route([lat, lng], [lat2, lng2],
                                                                       '2018-10-10T0' + str(hour) + ':00:00',
                                                              [herepy.RouteMode.car, herepy.RouteMode.fastest])
                    if flag == 0:
                        getRoutingData = routingApi.car_route([lat, lng], [lat2, lng2],
                                                                       '2018-10-10T' + str(hour) + ':00:00',
                                                              [herepy.RouteMode.car, herepy.RouteMode.fastest])

                    RoutingData = getRoutingData.as_dict()

                    carTraffictime = RoutingData['response']['route'][0]['summary']['trafficTime']
                    carTraffictime = int(carTraffictime) / 60
                    time.sleep(0.1)

                    # if flag == 1:
                    #     getPRoutingData = ProutingApi.public_transport([lat, lng], [lat2, lng2], True, '2018-10-10T0'+str(hour)+':00:00',[herepy.RouteMode.publicTransport, herepy.RouteMode.fastest])
                    # if flag == 0:
                    #     getPRoutingData = ProutingApi.public_transport([lat, lng], [lat2, lng2], True,'2018-10-10T' + str(hour) + ':00:00',[herepy.RouteMode.publicTransport,herepy.RouteMode.fastest])
                    #
                    # PublicRoutingData = getPRoutingData.as_dict()
                    #
                    # PTbasetime = PublicRoutingData['response']['route'][0]['summary']['baseTime']
                    # PTbasetime = int(PTbasetime) / 60
                    # time.sleep(0.1)

                    data.loc[i, title] = carTraffictime
                   # data.loc[i, 'Car'] = carTraffictime
                except:
                    data.loc[i, title] = 'Retry'

        return data





       ########## OUTPUT DATA #############


    totalRouting_output = totalRouting_dataset(fpath, 'Origin','Destination')
    totalRouting_output.to_excel(totalOutput_path)



import sys
import numpy as np
import pandas as pd
import time
import herepy
#from pandasql import sqldf
import datetime

#### USER INPUTS #####

# fpath = sys.argv[1]
# column_name = sys.argv[2]

fpath = "C:/Skyhook/HERE/Uk/separate/Book11.xlsx"
#fpath = "C:/Skyhook/HERE/Input3.xlsx"
# output_path = "C:/Skyhook/HERE/geoOutput.xlsx"
carOutput_path = "C:/Skyhook/HERE/CarOutput1am.xlsx"
# publicOutput_path = "C:/Skyhook/HERE/PublicOutput.xlsx"
# walkOutput_path = "C:/Skyhook/HERE/WalkOutput.xlsx"
# totalOutput_path = "C:/Skyhook/HERE/totalOutput.xlsx"
# column_name = 'final_address'

data = pd.read_excel(fpath)
########################### DO NOT CHANGE BELOW #######################


#### CREDENTIALS ####

credentials = np.load(r"C:\Skyhook\HERE\HERE_API_credentials.npy")

# apiID = 'vQUXblWlsSzsBSJNRDax'
# apiCode = 'f4f3xSQqZX5l3m6ur86jAQ'

appID = credentials[1]
appCode = credentials[2]


############# FUNCTIONS ########################

def geocode(apiID, apiCode, address):
    appID = apiID
    appCode = apiCode

    geocoderApi = herepy.GeocoderApi(appID, appCode)

    geoCodeResponse = geocoderApi.free_form(address)

    data = geoCodeResponse.as_dict()

    lat = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
    lon = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
    relevance = data['Response']['View'][0]['Result'][0]['Relevance']
    matchLevel = data['Response']['View'][0]['Result'][0]['MatchLevel']
    matchQuality = str(data['Response']['View'][0]['Result'][0]['MatchQuality'])
    matchType = data['Response']['View'][0]['Result'][0]['MatchType']
    resultAddress = data['Response']['View'][0]['Result'][0]['Location']['Address']['Label']

    print("Latitude: ", lat)
    print("Longitude: ", lon)

    time.sleep(0.1)

    return (lat, lon, relevance, matchLevel, matchQuality, matchType, resultAddress)

####################################################################


def carRouting(apiID, apiCode, orig, dest):
    appID = apiID
    appCode = apiCode


    routingApi = herepy.RoutingApi(appID, appCode)

    lat, lng = map(float, orig.strip('()').split(','))
    lat2, lng2 = map(float, dest.strip('()').split(','))

    getRoutingData = routingApi.car_route([lat,lng], [lat2,lng2], [herepy.RouteMode.car, herepy.RouteMode.fastest])

    #print(getRoutingData)
    try:

        RoutingData= getRoutingData.as_dict()

        OriginLat = RoutingData['response']['route'][0]['waypoint'][0]['originalPosition']['latitude']
        Originlon = RoutingData['response']['route'][0]['waypoint'][0]['originalPosition']['longitude']
        DestLat = RoutingData['response']['route'][0]['waypoint'][0]['mappedPosition']['latitude']
        Destlon = RoutingData['response']['route'][0]['waypoint'][0]['mappedPosition']['longitude']
        traffictime = RoutingData['response']['route'][0]['summary']['trafficTime']
        traffictime = int(traffictime) / 60
        basetime = RoutingData['response']['route'][0]['summary']['baseTime']
        text = RoutingData['response']['route'][0]['summary']['text']
        text = text.replace("""<span class="length">""", "").replace("</span>", "").replace("""<span class="time">""","")
        time.sleep(0.1)

        return (OriginLat, Originlon, DestLat, Destlon, traffictime, basetime,text)

    except:

        OriginLat = np.nan
        Originlon = np.nan
        DestLat = np.nan
        Destlon = np.nan
        traffictime= np.nan
        basetime =np.nan
        text = np.nan
        return (OriginLat, Originlon, DestLat, Destlon, traffictime, basetime, text)

####################################################################



def publicRouting(apiID, apiCode, orig, dest):
    appID = apiID
    appCode = apiCode


    ProutingApi = herepy.RoutingApi(appID, appCode)

    lat, lng = map(float, orig.strip('()').split(','))
    lat2, lng2 = map(float, dest.strip('()').split(','))

    getPRoutingData = ProutingApi.public_transport([lat,lng], [lat2,lng2],True, [herepy.RouteMode.publicTransport, herepy.RouteMode.fastest])


    try:

        PublicRoutingData= getPRoutingData.as_dict()


        OriginLat = PublicRoutingData['response']['route'][0]['waypoint'][0]['originalPosition']['latitude']
        Originlon = PublicRoutingData['response']['route'][0]['waypoint'][0]['originalPosition']['longitude']
        DestLat = PublicRoutingData['response']['route'][0]['waypoint'][0]['mappedPosition']['latitude']
        Destlon = PublicRoutingData['response']['route'][0]['waypoint'][0]['mappedPosition']['longitude']
        basetime = PublicRoutingData['response']['route'][0]['summary']['baseTime']
        basetime = int(basetime) / 60
        text = PublicRoutingData['response']['route'][0]['summary']['text']
        text = text.replace("""<span class="length">""", "").replace("</span>", "").replace("""<span class="time">""","")

        time.sleep(0.1)

        return (OriginLat, Originlon, DestLat, Destlon, basetime,text)

    except:
        OriginLat = np.nan
        Originlon = np.nan
        DestLat = np.nan
        Destlon = np.nan
        basetime =np.nan
        text = np.nan
        return (OriginLat, Originlon, DestLat, Destlon, basetime, text)

####################################################################



def walkRouting(apiID, apiCode, orig, dest):
    appID = apiID
    appCode = apiCode


    WroutingApi = herepy.RoutingApi(appID, appCode)

    lat, lng = map(float, orig.strip('()').split(','))
    lat2, lng2 = map(float, dest.strip('()').split(','))

    getWRoutingData = WroutingApi.pedastrian_route([lat,lng], [lat2,lng2], [herepy.RouteMode.pedestrian, herepy.RouteMode.fastest])


    try:

        WalkRoutingData= getWRoutingData.as_dict()


        OriginLat = WalkRoutingData['response']['route'][0]['waypoint'][0]['originalPosition']['latitude']
        Originlon = WalkRoutingData['response']['route'][0]['waypoint'][0]['originalPosition']['longitude']
        DestLat = WalkRoutingData['response']['route'][0]['waypoint'][0]['mappedPosition']['latitude']
        Destlon = WalkRoutingData['response']['route'][0]['waypoint'][0]['mappedPosition']['longitude']
        basetime = WalkRoutingData['response']['route'][0]['summary']['baseTime']
        basetime = int(basetime) / 60
        text = WalkRoutingData['response']['route'][0]['summary']['text']
        text = text.replace("""<span class="length">""", "").replace("</span>", "").replace("""<span class="time">""","")


        time.sleep(0.1)


        return (OriginLat, Originlon, DestLat, Destlon, basetime,text)

    except:
        OriginLat = np.nan
        Originlon = np.nan
        DestLat = np.nan
        Destlon = np.nan
        basetime =np.nan
        text = np.nan
        return (OriginLat, Originlon, DestLat, Destlon, basetime, text)


####################################################################
def geocode_dataset(fpath, column_name):
    try:
        data = pd.read_excel(fpath)

    except:

        try:
            data = pd.read_csv(fpath)

        except:
            "Input File Read Error!! Please check Format."

    for i in range(len(data)):

        try:
            result = geocode(appID, appCode, data.loc[i, column_name])

        except:

            result = (np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan)

        data.loc[i, 'lat'] = result[0]
        data.loc[i, 'lon'] = result[1]
        data.loc[i, 'Relevance'] = result[2]
        data.loc[i, 'Match_Level'] = result[3]
        data.loc[i, 'Match_Quality'] = result[4]
        data.loc[i, 'Match_Type'] = result[5]
        data.loc[i, 'ResultAddress'] = result[6]

        print(i, ": Lat - ", result[0], ", Lon - ", result[1])

    return data

####################################################################

def carRouting_dataset(fpath, column_name1, column_name2  ):
    try:
        data = pd.read_excel(fpath)

    except:

        try:
            data = pd.read_csv(fpath)

        except:
            "Input File Read Error!! Please check Format."

    for i in range(len(data)):

        result = carRouting(appID, appCode, data.loc[i, column_name1],data.loc[i, column_name2])


        #print(data)
        #data.loc[i, 'OriginLat'] = result[0]
        #data.loc[i, 'Originlon'] = result[1]
        #data.loc[i, 'DestLat'] = result[2]
        #data.loc[i, 'Destlon'] = result[3]
        data.loc[i, 'traffictime'] = result[4]
        #data.loc[i, 'basetime'] = result[5]
        #data.loc[i, 'text'] = result[6]
        #
        # print(i, ": Lat - ", result[0], ", Lon - ", result[1])

    return data

####################################################################

def publicRouting_dataset(fpath, column_name1, column_name2  ):
    try:
        data = pd.read_excel(fpath)

    except:

        try:
            data = pd.read_csv(fpath)

        except:
            "Input File Read Error!! Please check Format."

    for i in range(len(data)):

        result = publicRouting(appID, appCode, data.loc[i, column_name1],data.loc[i, column_name2])


        #print(data)
        data.loc[i, 'OriginLat'] = result[0]
        data.loc[i, 'Originlon'] = result[1]
        data.loc[i, 'DestLat'] = result[2]
        data.loc[i, 'Destlon'] = result[3]
        data.loc[i, 'basetime'] = result[4]
        data.loc[i, 'text'] = result[5]

        #
        # print(i, ": Lat - ", result[0], ", Lon - ", result[1])

    return data

####################################################################

def walkRouting_dataset(fpath, column_name1, column_name2  ):
    try:
        data = pd.read_excel(fpath)

    except:

        try:
            data = pd.read_csv(fpath)

        except:
            "Input File Read Error!! Please check Format."

    for i in range(len(data)):

        result =walkRouting(appID, appCode, data.loc[i, column_name1],data.loc[i, column_name2])


        #print(data)
        data.loc[i, 'OriginLat'] = result[0]
        data.loc[i, 'Originlon'] = result[1]
        data.loc[i, 'DestLat'] = result[2]
        data.loc[i, 'Destlon'] = result[3]
        data.loc[i, 'Basetime in seconds'] = result[4]
        data.loc[i, 'Text output'] = result[5]

        #
        # print(i, ": Lat - ", result[0], ", Lon - ", result[1])

    return data





####################################################################

def totalRouting_dataset(fpath, column_name1, column_name2  ):
    try:
        data = pd.read_excel(fpath)

    except:

        try:
            data = pd.read_csv(fpath)

        except:
            "Input File Read Error!! Please check Format."

    for i in range(len(data)):

        result = (
                  walkRouting(appID, appCode, data.loc[i, column_name1], data.loc[i, column_name2]) +
                  publicRouting(appID, appCode, data.loc[i, column_name1], data.loc[i, column_name2])+
                  carRouting(appID, appCode, data.loc[i, column_name1], data.loc[i, column_name2])
                  )

        # print(data)
        data.loc[i, 'Walking Basetime'] = result[4]
        #data.loc[i, 'Text output Walking'] = result[5]
        data.loc[i, 'Public transport Basetime'] = result[10]
        #data.loc[i, 'Text output Public Transport'] = result[11]
        data.loc[i, 'Car Traffic Time'] = result[16]
        #data.loc[i, 'Car Basetime'] = result[17]
        #data.loc[i, 'Text output Car'] = result[18]
        #
        # print(i, ": Lat - ", result[0], ", Lon - ", result[1])

    return data


####################################################################
#
# def totalRouting_sum():
#     totalRouting_output = totalRouting_dataset(fpath, 'Origin','Destination')
#
#     df = pd.DataFrame(totalRouting_output)
#     df['Closest Hospital'] = ""
#     #for i in range(len(totalRouting_output)):
#         #totalRouting_output.loc[i, 'Testo'] = 'AHAHA'
#     # for column in df:
#     #     df['Closest Hospital'] = sqldf("select Destination from df group by Origin order by `Car Basetime in seconds` desc limit 1 ", locals())
# 
#
#
#     return df



########## OUTPUT DATA #############


#geocoding_output = geocode_dataset(fpath, 'final_address')
#geocoding_output.to_excel(output_path)

carRouting_output = carRouting_dataset(fpath, 'Origin','Destination')
carRouting_output.to_excel(carOutput_path)

# publicRouting_output = publicRouting_dataset(fpath, 'Origin','Destination')
# publicRouting_output.to_excel(publicOutput_path)

# walkRouting_output = walkRouting_dataset(fpath, 'Origin','Destination')
# walkRouting_output.to_excel(walkOutput_path)
#
# totalRouting_output = totalRouting_dataset(fpath, 'Origin','Destination')
# totalRouting_output.to_excel(totalOutput_path)


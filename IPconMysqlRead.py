#!/usr/bin/env python
import sys
import urllib.request
import json
import pymysql
import pandas as pd
from sqlalchemy import *


def get_info(adress):
    print("************************************************")

    api = "http://freegeoip.net/json/" + adress
    try:
        result = urllib.request.urlopen(api).read()
        result = str(result)
        result = result[2:len(result)-3]
        result = json.loads(result)
    except:
        print("Could not find: ", adress)
        return None


    print(adress)
    print("IP: ", result["ip"])
    print("Country Name: ", result["country_name"])
    print("Country Code: ", result["country_code"])
    print("Region Name: ", result["region_name"])
    print("Region Code: ", result["region_code"])
    print("City: ", result["city"])
    print("Zip Code: ", result["zip_code"])
    print("Latitude: ", result["latitude"])
    print("Longitude: ", result["longitude"])
    print("Location link: " + "http://www.openstreetmap.org/#map=11/" + str(result["latitude"]) +"/" + str(result["longitude"]))
    i = table.update()
    i.execute(lat=result["latitude"], lon=result["longitude"])
# def showhelp():
#     print ("Usage: geoip address [address]...")
#     print ("find gelocation of IP addresses and host names, using http://freegeoip.net/")
#
# if __name__ == "__main__": #code to execute if called from command-line
#     inputs = sys.argv
#     if len(inputs) < 2 or "--help" in inputs:
#         showhelp()
#     else:
#         for address in inputs[1:]:
#             get_info(address)
#         print("************************************************")

###############################################################
mysqlcon = 'mysql+pymysql://'+ 'root'+ ':' + 'Mentira$12' + '@' + 'localhost'+':'+ '3306/' + "test"+'?charset=utf8'
engine = create_engine(mysqlcon, encoding='utf-8')
metadata = MetaData(engine)
table = Table('IP', metadata, autoload=True)
s = table.select()
rs = s.execute()
rows = rs.fetchall()
for row in rows:
    get_info(str(row['ip']))
    # i = table.insert()
    # i.execute(lat=result["latitude"], lon=result["longitude"])
# print('IP:', row['ip'])

############################################################
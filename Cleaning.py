import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import glob
import numpy as np
import re

#########################GET INFO AND OUTLIERS
# df = pd.read_csv(r'C:\Skyhook\Helsingborg\Hel1.csv' , sep=',', encoding = "ANSI")
# print('df.head()')
# print(df.head())
# print('df.tail()')
# print(df.tail())
# print('df.columns')
# print(df.columns)
# print('df.shape')
# print(df.shape)
# print('df.info()')
# print(df.info())
# print('df.ProductLine.value_counts(dropna=False)')
# print(df.ProductLine.value_counts(dropna=False))
# print(df.ProductLine.value_counts(dropna=False).head())
# print('df.describe()')
# print(df.describe())
# print('df.population.plot(hist)')
# df.Sales.plot('hist')
# plt.show()
# df.boxplot(column='Sales', by='ProductLine')
# plt.show()

###############################################ALL CSV TO PANDAS##################


csv_files = glob.glob(r'C:\Users\Ricardo Jose Chaves\Box Sync\HERE_UK_WIP\Car\3-1am uk\*.xlsx')

print(csv_files)
list_data = []
for filename in csv_files:
    data = pd.read_excel(filename)
    list_data.append(data)
new=pd.concat(list_data)
new.to_excel(r'C:\Users\Ricardo Jose Chaves\Box Sync\HERE_UK_WIP\Car\3-1am uk\totalam.xlsx')
#pd.merge(left=state_populations, right=state_codes,on=None, left_on='state', right_on='name')

# ####################################################### MELT FROM COLUMNS TO ROWS###########################
# df = pd.read_csv(r'C:\Skyhook\Helsingborg\NewOne2.csv' , sep=',', encoding = "ANSI")
#
# # df2=pd.melt(frame=df, id_vars=['District','Country','CustName','CustNumber','Equipment/Aftermarket','RevenueType'],value_vars=['2015', '2016','2017'],var_name='Year', value_name='result')
# # df2.to_csv(r'C:\Skyhook\Helsingborg\NewOne.csv', sep=',')
#
# #########################################GROUP BY, INDEX####################################################
#
# #df.index.names = ['A']
# #print(df.groupby('District')[['2015','2016']].mean())
# #df3=df.pivot(index='A', columns='District', values='2015')
#
#
# #test
# ##################################Transform columns
# df['Country'] = df['Country'].astype(str)
# df['2015'] = pd.to_numeric(df['2017'],errors='coerce',downcast='double')
#
# ###regular expresion
# pattern = re.compile('\$\d*\.\d{2}')
# result = pattern.match('$17.89')
# print(bool(result))
# df['2015'] = df['2015'].astype(str)
# print(df['2015'].str.contains('\$\d*\.\d{2}',regex =True))
# print()
# print()
# print()
# print()
#
# ######################## de horas a minutos
#
# text = WalkRoutingData['response']['route'][0]['summary']['text']
# # text = text.replace("""The trip takes <span class="length">""", "").replace("</span>", "").replace("""km and <span class="time">""", "").replace(" h.", "")
# try:
#     a, b = text[74:79].split(":")
#     text = int(a) * 60 + int(b)
# except ValueError:
#     text = text[74:79]
#     print("Error Conversion a minutos")
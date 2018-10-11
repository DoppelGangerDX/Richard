
import pymysql
import pandas as pd
from sqlalchemy import create_engine
# import tkinter as tk
# from tkinter import filedialog
import numpy as np
from pathlib import Path
from datetime import datetime

#Connection String
mysqlcon = 'mysql+pymysql://'+ 'root'+ ':' + 'Mentira$12' + '@' + 'localhost'+':'+ '3306/' + "test"+'?charset=utf8'

#to be used for file selection
# root = tk.Tk()
# root.withdraw()
# file_path = filedialog.askopenfilename()


# def write_log(text, file):
#     f = open(file, 'a')
#     f.write("{}\n".format(text))
#     return
# logfile = r"C:\CSV4R\log.txt"


directory_in_str=r'C:\Skyhook\SQL'
pathlist = Path(directory_in_str).glob('**/*.csv')
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    print(path_in_str)


###### insert part
    try:
        engine = create_engine(mysqlcon, encoding='ANSI')
        print("... Connected to db using sqlalchemy")
    except:
        print("... Failed connecting to db using sqlalchemy")

    df = pd.read_csv(path_in_str , sep=',', encoding = "ANSI")
    #print(df.head())
    # s = df['pointtime'].apply(lambda x: x.split('T'))
    # df['Day'] = s.apply(lambda x: x[0])
    # df['Hour'] = s.apply(lambda x: x[1])

   #  ###########print info

   #  ###########print one column
   # # print(df.loc[55])
    #df.columns = df.columns.str.replace('\s', '')


    #df['Year'] = 2019


    #print(df.info(verbose=True))
    #print(len(df.columns))
    # filter_Start = [col for col in df.iloc[:,0:27]]
    #
    # #print(df[filter_Start])
    # filter_col = [col for col in df if col.startswith('Adj. FTE')]
    # dt2= df[filter_Start+filter_col]
    # dt2.columns = dt2.columns.str.replace('Adj. FTE : ', '')
    # dt3 = df[filter_Start + filter_col]



    dt2=df

    dt2.insert(loc=22, column='Initiative', value='Initative1')
    dt2.columns = dt2.columns.str.replace('Initative1', '')
    #columns19= ~dt2.columns.str.contains('20')
    dt2= dt2[dt2.columns[~dt2.columns.str.contains('Initative')]]


    #  dt2=pd.concat([dt2] * 6)
   #
   #  #########################################################
   #  filter_stack = [col for col in dt2.iloc[:, 0:27]]
   #  dt2 = dt2.stack().reset_index()
   #  dt2.columns = ['One', 'Two', 'Three']
   #  dt2.insert(loc=3, column='Year', value=2019)
   #  dt2.insert(loc=4, column='Half', value='H1')
   #  dt2.insert(loc=5, column='Initiative', value='Initiative 1')
   #  dt2.insert(loc=6, column='Result', value=0)
   #
   #
   #  dt2['Year'] = np.where((dt2['Two'].str.contains('2019') == True), '2019', '')
   #  dt2['Year'] = np.where((dt2['Two'].str.contains('2019')==True), '2019', dt2['Year'])
   #  dt2['Year'] = np.where((dt2['Two'].str.contains('2020') == True), '2020', dt2['Year'])
   #  dt2['Year'] = np.where((dt2['Two'].str.contains('2021') == True), '2021', dt2['Year'])
   #
   #  dt2['Half'] = np.where((dt2['Two'].str.contains('H1') == True), 'H1', '')
   #  dt2['Half'] = np.where((dt2['Two'].str.contains('Total') == True), 'Total', dt2['Half'])
   #  dt2['Half'] = np.where((dt2['Two'].str.contains('Run-rat') == True), 'Run-rat', dt2['Half'])
   #  dt2['Half'] = np.where((dt2['Two'].str.contains('H1') == True), 'H1', dt2['Half'])
   #  dt2['Half'] = np.where((dt2['Two'].str.contains('H2') == True), 'H2', dt2['Half'])
   #
   #
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 1') == True), 'Initiative1', '')
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Total') == True), 'Total', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 1') == True), 'Initiative1', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 2') == True), 'Initiative2', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 3') == True), 'Initiative3', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 4') == True), 'Initiative4', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 5') == True), 'Initiative5', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 6') == True), 'Initiative6', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 7') == True), 'Initiative7', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 8') == True), 'Initiative8', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 9') == True), 'Initiative9', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 10') == True), 'Initiative10', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 11') == True), 'Initiative11', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 12') == True), 'Initiative12', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 13') == True), 'Initiative13', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 14') == True), 'Initiative14', dt2['Initiative'])
   #  dt2['Initiative'] = np.where((dt2['Two'].str.contains('Initiative 15') == True), 'Initiative15', dt2['Initiative'])
   #
   #  dt2['Result'] = dt2['Three']
   #
   #
   #  dt2=dt2[['Two','Year','Half','Initiative','Result']].copy()
   #
   # #unstacked_df1 = dt2.unstack('Two', 'Result')
   #
   #  dt2=dt2.pivot_table(columns="Two", aggfunc='first')
   #  ####################################
   # # dt2.set_index(['Two']).unstack('Two')
   #  stacked_df = dt3.stack(dropna=False)
   #  print(stacked_df.head(25))
   #  dt2 = dt2.unstack().reset_index()
   # df['ShipDate'] =df['ShipDate'].str.replace('\s+', '')
   # df['ShipDate']=pd.to_datetime(df['ShipDate'], format='%m/%d/%Y')
   # df['Date'] = df['Date'].str.replace('\s+', '')
   # df['Hour']=pd.to_datetime(df['Hour'],format='%H:%M:%S')
   #  #df['Order'] = df['Order'].astype(str)
   #
   #  df['FixedCharge'] = pd.to_numeric(df['FixedCharge'], errors='coerce', downcast='float')
   #  df['UsageValue'] = pd.to_numeric(df['UsageValue'], errors='coerce', downcast='float')
   #
   # print(df.info(verbose=True))
    dt2.to_sql(name='Order', con=engine, if_exists='append',index=False,chunksize=10000)

   # write_log('\n'+path_in_str+' was processed at  '+str(datetime.now()), logfile)  # Write the specified text to the logfile

###end insert
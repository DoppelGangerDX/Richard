
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
from pathlib import Path
import time



###########Read File


#############Replace this path fo the path in your Laptop, nothing else needs to be changed

directory_in_str=r'C:\Skyhook\SQL\Test'


start_time = time.time()
pathlist = Path(directory_in_str).glob('**/*.csv')
i= 1
for path in pathlist:
    path_in_str = str(path)
    out = r'\Out' + str(i)
    output_path = directory_in_str + out + ".xlsx"


# ## connection to SQL
#
#     mysqlcon = 'mysql+pymysql://'+ 'root'+ ':' + 'Mentira$12' + '@' + 'localhost'+':'+ '3306/' + "test"+'?charset=utf8'
#
# ###### insert part
#     try:
#         engine = create_engine(mysqlcon, encoding='ANSI')
#         print("... Connected to db using sqlalchemy")
#     except:
#         print("... Failed connecting to db using sqlalchemy")

    ###########Process Information

    df = pd.read_csv(path_in_str , sep=',', encoding = "ANSI")
    df.columns = df.columns.str.replace('$', '')
    df.columns = df.columns.str.replace('?', '')
    df.columns = df.columns.str.replace('$', '')
    df.columns = df.columns.str.replace('#', '')



    dt1=df.copy()
    dt1.insert(loc=15, column='InitName', value='Initiative 1')
    dt1.columns = dt1.columns.str.replace('Initiative 1', '')
    dt1= dt1[dt1.columns[~dt1.columns.str.contains('Initiative')]]


    dt2 = df.copy()
    dt2.insert(loc=15, column='InitName', value='Initiative 2')
    dt2.columns = dt2.columns.str.replace('Initiative 2', '')
    dt2 = dt2[dt2.columns[~dt2.columns.str.contains('Initiative')]]

    dt3 = df.copy()
    dt3.insert(loc=15, column='InitName', value='Initiative 3')
    dt3.columns = dt3.columns.str.replace('Initiative 3', '')
    dt3 = dt3[dt3.columns[~dt3.columns.str.contains('Initiative')]]

    dt4 = df.copy()
    dt4.insert(loc=15, column='InitName', value='Initiative 4')
    dt4.columns = dt4.columns.str.replace('Initiative 4', '')
    dt4 = dt4[dt4.columns[~dt4.columns.str.contains('Initiative')]]

    dt5 = df.copy()
    dt5.insert(loc=15, column='InitName', value='Initiative 5')
    dt5.columns = dt5.columns.str.replace('Initiative 5', '')
    dt5 = dt5[dt5.columns[~dt5.columns.str.contains('Initiative')]]

    dt6 = df.copy()
    dt6.insert(loc=15, column='InitName', value='Initiative 6')
    dt6.columns = dt6.columns.str.replace('Initiative 6', '')
    dt6 = dt6[dt6.columns[~dt6.columns.str.contains('Initiative')]]

    dt7 = df.copy()
    dt7.insert(loc=15, column='InitName', value='Initiative 7')
    dt7.columns = dt7.columns.str.replace('Initiative 7', '')
    dt7 = dt7[dt7.columns[~dt7.columns.str.contains('Initiative')]]

    dt8 = df.copy()
    dt8.insert(loc=15, column='InitName', value='Initiative 8')
    dt8.columns = dt8.columns.str.replace('Initiative 8', '')
    dt8 = dt8[dt8.columns[~dt8.columns.str.contains('Initiative')]]

    dt9 = df.copy()
    dt9.insert(loc=15, column='InitName', value='Initiative 9')
    dt9.columns = dt9.columns.str.replace('Initiative 9', '')
    dt9 = dt9[dt9.columns[~dt9.columns.str.contains('Initiative')]]

    dt10 = df.copy()
    dt10.insert(loc=15, column='InitName', value='Initiative 10')
    dt10.columns = dt10.columns.str.replace('Initiative 10', '')
    dt10 = dt10[dt10.columns[~dt10.columns.str.contains('Initiative')]]

    dt11 = df.copy()
    dt11.insert(loc=15, column='InitName', value='Initiative 11')
    dt11.columns = dt11.columns.str.replace('Initiative 11', '')
    dt11 = dt11[dt11.columns[~dt11.columns.str.contains('Initiative')]]

    dt12 = df.copy()
    dt12.insert(loc=15, column='InitName', value='Initiative 12')
    dt12.columns = dt12.columns.str.replace('Initiative 12', '')
    dt12= dt12[dt12.columns[~dt12.columns.str.contains('Initiative')]]

    dt13 = df.copy()
    dt13.insert(loc=15, column='InitName', value='Initiative 13')
    dt13.columns = dt13.columns.str.replace('Initiative 13', '')
    dt13 = dt13[dt13.columns[~dt13.columns.str.contains('Initiative')]]

    dt14 = df.copy()
    dt14.insert(loc=15, column='InitName', value='Initiative 14')
    dt14.columns = dt14.columns.str.replace('Initiative 14', '')
    dt14 = dt14[dt14.columns[~dt14.columns.str.contains('Initiative')]]

    dt15 = df.copy()
    dt15.insert(loc=15, column='InitName', value='Initiative 15')
    dt15.columns = dt15.columns.str.replace('Initiative 15', '')
    dt15 = dt15[dt15.columns[~dt15.columns.str.contains('Initiative')]]

    frames = [dt1, dt2, dt3, dt4, dt5, dt6, dt7, dt8, dt9, dt10, dt11, dt12, dt13, dt14, dt15]

    result = pd.concat(frames, axis=0)


    cols = dt2.columns
    result = result[cols]
    result.columns = result.columns.str.replace(' : ', '')



    ###Print Information##############

    #print(df.info(verbose=True))
    #print(dt1.info(verbose=True))
    #print(dt1.columns)

    #########OUTPUTS###################

    # output to SQL
    #result.to_sql(name='Order', con=engine, if_exists='append',index=False,chunksize=10000)

    #Output to Excel
    result.to_excel(output_path)
    elapsed_time = time.time() - start_time
    print('Elapsed time was: ' + str(round(elapsed_time, 2)) + ' sec')

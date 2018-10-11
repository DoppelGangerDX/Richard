
import pandas as pd
import numpy as np
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import json
from sqlalchemy import create_engine, MetaData
import random
import io
import glob
import time
from enum import Enum
import datetime
import os

os.chdir(r'/root/Documents/')

connector = "postgresql+psycopg2://" + 'postgres' + ":" + 'r' + "@"+'localhost'+":"+str(5432)+"/" + 'Test1'
#print(connector)

try:
    engine = create_engine(connector)
    print("... Connected to DB")
except:
    print("... Failed connecting to DB")




# df = pd.DataFrame()
# dfLen = 10000
# dfCols = 10
# for x in range(0, dfCols):
#     colName = 'a' + str(x)
#     df[colName] = [random.randint(0, 99) for x in range(1,dfLen)]



from sqlalchemy import types as sql_types

# flight_sqltypes = {'PARTY_ID':sql_types.TEXT,'LYLTY_LEVEL_CD':sql_types.TEXT,'OA_LYLTY_PGM_OWN_CD':sql_types.TEXT,'OA_LYLTY_LEVEL_CD':sql_types.TEXT,
# 'PNR_LOCTR_ID':sql_types.TEXT,'PNR_CREATE_DT':sql_types.TEXT,'PNR_CREATE_TM':sql_types.TEXT,'ACCT_AIRLN_IATA_CD':sql_types.TEXT,
# 'TICKET_NBR':sql_types.TEXT,'TICKET_ISSUE_DT':sql_types.TEXT,'SEG_DEP_DT':sql_types.TEXT,'MKT_AIRLN_IATA_CD':sql_types.TEXT,'MKT_FLIGHT_NBR':sql_types.TEXT}
#
# flight_dtypes = {'PARTY_ID':str,'LYLTY_LEVEL_CD':str,'OA_LYLTY_PGM_OWN_CD':str,'OA_LYLTY_LEVEL_CD':str,
# 'PNR_LOCTR_ID':str,'PNR_CREATE_DT':str,'PNR_CREATE_TM':str,'ACCT_AIRLN_IATA_CD':str,
# 'TICKET_NBR':str,'TICKET_ISSUE_DT':str,'SEG_DEP_DT':str,'MKT_AIRLN_IATA_CD':str,'MKT_FLIGHT_NBR':str}

df = pd.read_csv('20151204.csv', encoding='ISO-8859-1',error_bad_lines=False)
df=df.fillna(0)
# df['yyyymmdd'] = pd.to_datetime(df['yyyymmdd'], format='%Y%m%d')
# df['flt_dptr_date_d'] = df['flt_dptr_date_d'].str.replace('T05:00:00Z+', '')
# df['flt_dptr_date_d'] = pd.to_datetime(df['flt_dptr_date_d'], format='%Y-%m-%d')
# df['cabin_code_c'] = df['cabin_code_c'].astype(str)


flight_sqltypes = {'yyyymmdd':sql_types.Date,'flt_id_i':sql_types.INTEGER,'flt_dptr_date_d':sql_types.Date,'cabin_code_c':sql_types.Text,
'cap_i':sql_types.INTEGER,'sabre_auth_level_i':sql_types.INTEGER,'res_hold_total_i':sql_types.INTEGER,'flow_ebp_f':sql_types.Float,
'lcl_ebp_f':sql_types.Float}

#
# def cleanColumns(columns):
#     cols = []
#     for col in columns:
#         col = col.replace(' ', '_')
#         cols.append(col)
#     return cols
#
def to_pg(df, table_name, con):
    data = io.StringIO()
    #df.columns = cleanColumns(df.columns)
    df.to_csv(data, header=False, index=False)
    data.seek(0)
    raw = con.raw_connection()
    curs = raw.cursor()
    curs.execute("DROP TABLE " + table_name)
    empty_table = pd.io.sql.get_schema(df, table_name, con = con,dtype= flight_sqltypes)
    empty_table = empty_table.replace('"', '')
    curs.execute(empty_table)
    curs.copy_from(data, table_name, sep = ',')

    curs.connection.commit()



start_time = time.time()
to_pg(df,'Test1',engine)
elapsed_time = time.time() - start_time
print('1Elapsed time in write_files_to_db was: '+ str(round(elapsed_time,2))+ ' sec')




start_time = time.time()
df.to_sql(name='test1', con=engine, if_exists='replace',index=False,chunksize=10000)
elapsed_time = time.time() - start_time
print('2Elapsed time in write_files_to_db was: '+ str(round(elapsed_time,2))+ ' sec')


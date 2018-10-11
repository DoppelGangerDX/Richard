import pymysql
import pandas as pd
import pyodbc
from sqlalchemy import create_engine


##################ODBC direct method###########################
# con = pyodbc.connect('DSN=Exa')
# con.execute('OPEN SCHEMA TEST')
# data = pd.read_sql('SELECT * FROM HUB', con)

##############################################################################

#############SQL ALCHEMY#####################################

e = create_engine("exa+pyodbc://sys:exasol@Exa")
#r = e.execute("select 42 from dual").fetchall()

# st = e.execute("Select * from TEST.HUB")
# for row in st:
#    print(row)
data = pd.read_sql('SELECT * FROM HUB', e)
print(data.info(verbose=True))
#print(data)
##############################################################



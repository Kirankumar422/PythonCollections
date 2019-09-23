import os
from datetime import date

import cx_Oracle
import csv

dsnStr = cx_Oracle.makedsn("10.5.179.24", "1535", "OPTSA2")
con = cx_Oracle.connect(user="cyginv", password="welcome#123", dsn=dsnStr)
cur = con.cursor()
cur.execute('select * from ManagedObject')
result = cur.fetchmany(numRows=3)
print result[0]
cur.close()
con.close()

# print (con.version)
# print("DB connected")
# cursor = con.cursor()
# query = "select count(*) from CygnettoM6LabelMapping"
# cursor.execute(query)
# output = con.execute("select count(*) from CygnettoM6labelmapping")
# print("Query executed Successfully")


# import csv

# try:
#   con = cx_Oracle.connect('cyginv/cyginv@10.5.179.23:1535/OPTSA1')
#  print("Connected to db successfully")
# cursor = con.cursor()
# cursor.execute("select count(*) from cygnettom6labelmapping")
# print ("Query Executed successfully")

# except cx_Oracle.DatabaseError as e:
#   print("There is an issue in connecting to db", e)

# finally:
#   if con:
#      con.

# if con:


# sql = "select count(*) from cygnettom6labelmapping"

# filename = "/data/AIRTEL-SA_Cleaned_Label/output.csv"
# file = open(filename,"w");
# output = csv.writer(file,dialect="excel")
# connection = cx_Oracle.connection = cx_Oracle.connect('cyginv/cyginv@10.5.179.23:1535/OPTSA1')
# cursor = connection.cursor()
# cursor.execute(SQL)
# for row in cursor:
#   output.writerow(row)
# cursor.close()
# connection.close()
# file.close()

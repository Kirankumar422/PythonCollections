import cx_Oracle
import csv

dsn_tns = cx_Oracle.makedsn("localhost", "10100", "M621PRD")
con = cx_Oracle.connect(user="cygnetsa", password="Vodafone#1a2b", dsn=dsn_tns)
print ("DB Connected")
cur = con.cursor()
print ("Executing the query")
# query = """select distinct C.EXCHANGE_CARRIER_CIRCUIT_ID, NCA.CLLI_CODE ACODE, NCA.LOCATION_NAME ALOCATIONNAME, NCZ.CLLI_CODE ZCODE, NCZ.LOCATION_NAME,
# SI.DOCUMENT_NUMBER, RE.RESPONSIBLE_PARTY, P.AES_CORP_ID from circuit c, serv_item s, serv_req_si si, serv_req re, PSR_USER_DATA p,
# NETWORK_LOCATION nca, NETWORK_LOCATION ncz where c.type = 'S' and C.STATUS in ('1', '2', '3', '4', '5', '6', '7') and
# C.LOCATION_ID = NCA.LOCATION_ID and C.LOCATION_ID_2 = NCZ.LOCATION_ID and C.CIRCUIT_DESIGN_ID = S.CIRCUIT_DESIGN_ID and
# S.SERV_ITEM_ID = SI.SERV_ITEM_ID and SI.DOCUMENT_NUMBER = RE.DOCUMENT_NUMBER and RE.DOCUMENT_NUMBER = P.DOCUMENT_NUMBER and
# RE.RESPONSIBLE_PARTY is not null and P.AES_CORP_ID is not null"""
query = "select * from psr_user_data where aes_corp_id is not null"
# cur.execute('select * from ManagedObject')
# print date.
# cur.close()
# con.close()

# print (con.version)
# print("DB connected")
# cursor = con.cursor()
# query = "select count(*) from CygnettoM6LabelMapping"
#cursor.execute(query)
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

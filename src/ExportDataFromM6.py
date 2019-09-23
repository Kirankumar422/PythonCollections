import cx_Oracle
import timeit
dsn_tns = cx_Oracle.makedsn("localhost", "10100", "M621PRD")
con = cx_Oracle.connect(user="cygnetsa", password="Vodafone#1a2b", dsn=dsn_tns)
print ("DB Connected")
con = con.cursor()
print ("Executing the query")
tic = timeit.default_timer()  # before starting the process
query = """select count(*) from
(select distinct DOCUMENT_NUMBER, AES_CORP_ID from PSR_USER_DATA where DOCUMENT_NUMBER in
(select DOCUMENT_NUMBER from TEMP_DOC_NUMS_13_09))"""
con.execute(query)
res = con.fetchone()
toc = timeit.default_timer()   # after completion of the process
dif = toc - tic
print ("Time taken to fetch the output is {} secs".format(dif))
print ("Count of required table is {}".format(res[0]))
con.close()
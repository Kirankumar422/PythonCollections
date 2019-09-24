import cx_Oracle
import timeit
import csv


dsn_tns = cx_Oracle.makedsn("10.5.179.87", "1521", "OPTSAPT1")
con = cx_Oracle.connect(user="cyginv", password="cyginv", dsn=dsn_tns)
cursor = con.cursor()
printHeader = True
print ("Connected to db")

# query = """
# select TLZ.userlabel, TLZ.nativeemsname from ManagedObject mo, TopologicalLink tlz
# where mo.type = 'PTP' and mo.parentmoid in (select moid from me where PRODUCTNAME in
# ('OptiX OSN 1832 X8', 'OptiX OSN 1832 X16')) and
# mo.name = TLZ.aENDTP"""

# query = """select distinct TL.AENDTP, TL.ZENDTP, mo.name, EN.GROUP_ID, GR.GROUP_STATUS, GR.GROUP_TYPE from
# ((select distinct moid, AENDTP, ZENDTP from TopologicalLink where AENDTP in
# (select PTPNAME from temp_4lac_distinct_ports)) union
# (select distinct moid, ZENDTP, AENDTP from TopologicalLink where ZENDTP in
# (select PTPNAME from temp_4lac_distinct_ports))) tl, ManagedObject mo, INTV_LINK_ENTRIES en, INTV_LINK_GROUPS gr
# where tl.moid = mo.moid and
# mo.name = EN.LINK_NAME and EN.GROUP_ID = GR.GROUP_ID"""

# query = """select distinct m.name, bws.LAYERRATE from ManagedObject m, BANDWIDTHSERVICE bws where name in
# (select CIRCUITNAME from TEMP_4LAC_PW_BWS) and m.moid = bws.moid"""

# query = """select mo.name, CLS.TPNAME, CLS.MENAME from ManagedObject mo, CONNECTIONLESSSERVICEEND cls where mo.name in
# (select PTPNAME from TEMP_4LAC_PART4_CLS) and MO.MOID = CLS.MOID order by MO.name """

# query = "select distinct RESPONSIBLE_PARTY from ADRS_MAXORDER_2_9_2019"

# query = """select distinct TL.AENDTP, TL.ZENDTP, MO.name, EN.GROUP_ID, GR.GROUP_STATUS, GR.GROUP_TYPE,
# ERR.GROUP_ERROR_TYPE, ERR.ERROR_REASON from
# (select distinct moid, AENDTP, ZENDTP from TopologicalLink where AENDTP in
# (select PTPNAME from TEMP_4LAC_PART123_PORTS) union
# select distinct moid, ZENDTP, AENDTP from TopologicalLink where ZENDTP in
# (select PTPNAME from TEMP_4LAC_PART123_PORTS)) tl, ManagedObject mo, INTV_LINK_ENTRIES en, INTV_LINK_GROUPS gr, INTV_GROUP_ERROR_INFO err where
# TL.MOID = MO.MOID and MO.name = EN.LINK_NAME and EN.GROUP_ID = GR.GROUP_ID and GR.GROUP_ID = ERR.GROUP_ID"""

# query = """select distinct GROUP_ID, GROUP_ERROR_TYPE, ERROR_REASON from INTV_GROUP_ERROR_INFO where GROUP_ID in
# (select distinct GROUPID from TEMP_4LAC_PART4_GROUPIDS)"""

query = raw_input("Please enter the query: ")

print ("Executing the query")
tic = timeit.default_timer()
res = cursor.execute(query)
toc = timeit.default_timer()
dif = toc - tic
print ("Query executed successfully and time taken is {} ".format(dif))
fileName = raw_input("Please enter the path with filename to save output: ")
csv_file = open(fileName, 'w')
writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
print ("Writing the output to CSV Started...")
if printHeader:
    cols = []
    for col in cursor.description:
        cols.append(col[0])
    writer.writerow(cols)
for row in cursor:
    writer.writerow(row)
print ("CSV writing is completed and file is successfully stored in {} ".format(fileName))
cursor.close()
con.close()
csv_file.close()

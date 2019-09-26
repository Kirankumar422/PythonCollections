import mysql.connector
import timeit
import csv

database = raw_input("Please enter your database name: ")
mydb = mysql.connector.connect(host="localhost", user="kirankumar", password="kirankumar", database=database)
print ("Connected to database")
mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM cygnettom6label")
query = raw_input("Please enter the query: ")
print ("Executing the Query....")
tic = timeit.default_timer()
mycursor.execute(query)
toc = timeit.default_timer()
dif = toc - tic
print ("Query Executed successfully and time taken is {} secs".format(dif))
fileName = raw_input("Please enter the path with filename to save output: ")
csv_file = open(fileName, "w")
writer = csv.writer(csv_file, delimiter=",", lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
print ("Writing output to CSV started.....")
printHeader = True
if printHeader:
    cols = []
    for col in mycursor.description:
        cols.append(col[0])
    writer.writerow(cols)
for row in mycursor:
    writer.writerow(row)
print ("CSV writing is completed and output is stored in {}".format(fileName))
mycursor.close()
csv_file.close()

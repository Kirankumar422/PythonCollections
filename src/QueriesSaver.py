import csv
from datetime import date

date = date.today()
queryFile = '/home/kirankumar/Shared/Common Files/used_queries.csv'
readFile = open(queryFile, 'r')
printHeader = True
length = len(readFile.readlines())
print ("Total lines in file is {}".format(length))
if length >= 1:
    writeFile = open(queryFile, "a")
    writer = csv.writer(writeFile, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    while True:
        query = raw_input("Please enter query: ")
        desc = raw_input("Please enter the description of the query: ")
        writer.writerow([date, query, desc])
        writeFile.close()
        print (" Queries file is updated with new entries")
        break






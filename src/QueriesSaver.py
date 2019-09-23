import csv
from datetime import date

date = date.today()
query = raw_input("Please enter query: ")
desc = raw_input("Please enter the query description: ")
row = [date, query, desc]
with open('/home/kirankumar/Desktop/Kiran/used_queries.csv') as WriteFile:
    writer = csv.writer(WriteFile, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    row[0] = ["Date", ""]




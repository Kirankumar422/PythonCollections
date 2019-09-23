import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="kirankumar",password="kirankumar",database="m6db")
print ("Connected to database")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM cygnettom6label")
res = mycursor.fetchone()
print (res)
mycursor.close()
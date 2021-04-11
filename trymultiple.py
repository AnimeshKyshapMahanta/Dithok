import mysql.connector
from mysql.connector import errorcode
import csv


connection = mysql.connector.connect(user='root', password='root', host='localhost', database='multiple')
mycursor = connection.cursor()

file = open('Dithok2.csv')
csv_data = csv.reader(file)

skipHeader = True

for row in csv_data:
	if skipHeader:
		skipHeader = False
		continue
	mycursor.execute('INSERT INTO Studentinfo (idStudent, StudentName, Address, Hostel) VALUES ( %s, %s, %s, %s)',row[0:4])   
	Stdid = mycursor.lastrowid
	print(Stdid)
	mycursor.execute('INSERT INTO Studentmarks (idStudent, Class, Marks, Roll) VALUES (%(Stdid)s, %s, %s, %s)',row[4:7])

print('Data Succesfully Inserted')
connection.commit()
connection.close()
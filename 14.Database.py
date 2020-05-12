import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='anmol',passwd='password')
mycursor=mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='anmol',passwd='password',database='anmol')
mycursor=mydb.cursor()
mycursor.execute("select * from name")
for i in mycursor:
    print(i)
mycursor=mydb.cursor()
mycursor.execute("select * from name")
result=mycursor.fetchall()
for i in result:
    print(i)

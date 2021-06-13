#!/usr/bin/python3 

import mysql.connector as connector

db = connector.connect(host='localhost',
                       user='root',
                       passwd='arch')
c = db.cursor()
c.execute("use mysql;")
c.execute("select * from STUDENT where Name = \"" + input("Query: ") + "\";")
print(c.fetchall())
db.close()

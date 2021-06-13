#!/usr/bin/python3 

import mysql.connector as connector

db = connector.connect(host='localhost',
                       user='root',
                       passwd='arch')
c = db.cursor()
c.execute("use mysql;")
c.execute("insert into STUDENT " + input("Query: ") + ";")
db.commit() 
db.close()

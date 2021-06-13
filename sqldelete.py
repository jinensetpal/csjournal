#!/usr/bin/python3 

import mysql.connector as connector

db = connector.connect(host='localhost',
                       user='root',
                       passwd='arch')
c = db.cursor()
c.execute("use mysql;")
c.execute("delete from STUDENT where No = \"" + input("No.: ") + "\";")
db.commit() 
db.close()

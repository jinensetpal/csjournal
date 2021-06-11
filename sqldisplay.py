#!/usr/bin/python3 

import mysql.connector as connector

db = connector.connect(host='localhost',
                       user='root',
                       passwd='i_use_arch_btw')
c = db.cursor()
c.execute("select * from STUDENT where name = " + input("Query: "))
db.close()

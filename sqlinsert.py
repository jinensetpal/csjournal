#!/usr/bin/python3 

import mysql.connector as connector

db = connector.connect(host='localhost',
                       user='root',
                       passwd='i_use_arch_btw')
c = db.cursor()
c.execute("insert into STUDENT " + eval(input("Query: ")))
db.commit() 
db.close()

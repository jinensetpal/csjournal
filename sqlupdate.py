#!/usr/bin/python3 

import mysql.connector as connector

db = connector.connect(host='localhost',
                       user='root',
                       passwd='i_use_arch_btw')
c = db.cursor()
c.execute("update STUDENT set Name = " + input("Name: ") + ", Stipend " + input("Stipend: ") + ", Stream " + input("Stream") + ", AvgMark " + input("Average Marks: ") + ", Grade " + input("Grade: ") + ", Class " + input("Class: ") + "where No = " + input("No.: ") + ";")
db.commit() 
db.close()

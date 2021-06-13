#!/usr/bin/python3

import csv

l = []
while True:
    option = int(input("1: Add\n2: Search\n3: Exit\nSelect: "))
    if option == 1:
        l.append([int(input("Gr. No: ")), input("Name: "), input("Class: "), input("Section: ")])
    elif option == 2:
        if len(list([print(i) for i in l if i[0] == int(input("Query: "))])) == 0:
            print("Not found")
    else:
        with open('file.csv', 'w') as f:
            write = csv.writer(f)
            write.writerows(l)
            break

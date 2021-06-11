#!/usr/bin/python3

import csv

l = []
while True:
    option = int(input("1: Add\n2: Search\n3: Exit\nSelect: "))
    if option == 1:
        l.append([int(input("Gr. No: ")), input("Name: "), int(input("Marks: "))])
    elif option == 2:
        q = int(input("Query: "))
        if len(list([print(i) for i in l if i[0] == q])) == 0:
            print("Not found")
    else:
        with open('file.csv', 'w') as f:
            write = csv.writer(f)
            write.writerows(l)
            break

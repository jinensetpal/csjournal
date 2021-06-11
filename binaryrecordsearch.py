#!/usr/bin/python3

import numpy as np

l = []
while True:
    option = int(input("1: Add\n2: Search\n3: Exit\nSelect: "))
    if option == 1:
        l.append([input("Name: "), int(input("Cell No: ")), input("Email ID: ")])
    elif option == 2:
        q = input("Query: ")
        if len(list([print(i) for i in l if i[0] == q])) == 0:
            print("Not found")
    else:
        np.save("file", np.array(l), allow_pickle=True)
        break

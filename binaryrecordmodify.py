#!/usr/bin/python3

import numpy as np

l = []
while True:
    option = int(input("1: Add\n2: Update\n3: Delete\n4: Exit\nSelect: "))
    if option == 1:
        l.append([int(input("Gr. No: ")), input("Name: "), int(input("Marks: "))])
    elif option == 2:
        if len(list([eval('l[i][2] == input("Marks: ")') for i in range(len(l)) if l[i][0] == int(input("Query: "))])) == 0:
            print("Not found")
    elif option == 3:
        if len(list([l.pop(i) for i in range(len(l)) if l[i][0] == int(input("Query: "))])) == 0:
            print("Not found")
    else:
        np.save("file", np.array(l), allow_pickle=True)
        break

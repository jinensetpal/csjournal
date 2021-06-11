#!/usr/bin/python3

with open("file.txt", "r") as f:
    for i in f.readlines():
        for j in i.split():
            print(j, end="#")

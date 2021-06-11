#!/usr/bin/python3

import pprint

d = {"v": 0, "w": 0, "u": 0, "d": 0}
with open("files.txt", "r") as f:
    for i in f.readlines():
        for j in i.split():
            print(j[::-1], end=" ")
            
            d["w"] += 1            
            for k in j:
                if k.isdigit():
                    d["d"] += 1
                elif k in "aeiouAEIOU":
                    d["v"] += 1
                if k.isupper():
                    d["u"] += 1

pprint.pprint(d)

#!/usr/bin/python3 

import pprint

d = {"v": 0, "c": 0, "u": 0, "l": 0}
for i in input("Enter a string: "):
    if i in "aeiouAEIOU":
        d["v"] += 1
    elif i.isalpha():
        d["c"] += 1
    if i.isupper():
        d["u"] += 1
    elif i.islower():
        d["l"] += 1
        
pprint.pprint(d)

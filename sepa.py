#!/usr/bin/python3

l = []
with open("file.txt", "r") as f:
    l = f.readlines()

f = open("file.txt", "w")
nf = open("newfile.txt", "w")

for i in l:
    if "a" in i:
        nf.write(i)
    else:
        f.write(i)

f.close()
nf.close()

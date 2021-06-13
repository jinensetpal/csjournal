#!/usr/bin/python3

l = eval(input("Enter an even-length list: "))
print([j for k in [[l[i + 1], l[i]] for i in range(0, len(l), 2)] for j in k])

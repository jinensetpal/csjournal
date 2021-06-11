#!/usr/bin/python3

def primeornot(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

print(primeornot(int(input("Enter a number: "))))

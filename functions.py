#!/usr/bin/python3

def primeornot(n):
    for i in range(2, n // 2):
        if not n % i:
            return False
    return True

print(primeornot(int(input("Enter a number: "))))

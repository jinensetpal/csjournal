#!/usr/bin/python3

def isperfect(n):
    s = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0: 
            s += i
    return s == n

def isarmstrong(n):
    s = 0 
    for i in str(n):
        s += int(i) ** 3
    return s == n

n = int(input("Enter number: ")) 

print("Perfect Number:", isperfect(n), "\nArmstrong Number:", isarmstrong(n), "\nPalindrome Number:", str(n) == str(n)[::-1])

#!/usr/bin/python3

l = [{"rollno": input("Enter Roll. No: "), "name": input("Enter Name: "), "marks": int(input("Enter Marks: "))} for i in range(int(input("Enter number of entries: ")))]
print([i["name"] for i in l if i["marks"] > 75], "have more than 75 marks")

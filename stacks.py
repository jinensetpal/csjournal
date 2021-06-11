#!/usr/bin/python3

def insert(q):
    l.append(q)
    
def delete():
    l.pop()
    
def display():
    print(l[-1])
    
def search(q):
    if len(list([print("Found at position:", i) for i in range(len(l)) if l[i] == q])) == 0:
            print("Not found")
    
l = []
while True:
    option = int(input("1: Insert\n2: Delete\n3: Display\n4: Search\n5: Exit\nSelect: "))
    if option == 1:
        insert(input("Query: "))
    elif option == 2:
        delete()
    elif option == 3:
        display()
    elif option == 4:
        search(input("Query: "))
    else:
        break

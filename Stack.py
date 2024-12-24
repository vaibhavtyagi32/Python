#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     16-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Stack is the linear data structure
# it store the item in Last In First Out manner

# Stack Operations are
# 1: Push:-Inserting an element
# 2: Pop:-Deleting an element
# 3: Peek:-Display the Last element
# 4: Display:-Display the List

l=[]
while True:
    c=int(input('''
    1 Push operation
    2 Pop Operation
    3 Peek Operation
    4 Display Operation
    5 Exit
    '''))
    if c==1:
        n=int(input("Enter the value: "))
        l.append(n)
        print(l)
    elif c==2:
        if(len(l)==0):
            print("Empty list")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if(len(l)==0):
            print("Empty list")
        else:
            print("Last element value: ",l[-1])
    elif c==4:
        if(len(l)==0):
            print("Empty list")
        else:
            print("Display stack ",l)
    elif c==5:
        break;
    else:
        print("Invalid choice ")
        break;



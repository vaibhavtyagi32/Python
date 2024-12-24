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

# QUEUE
# The queue is the linear data structure
# it can store the item in First In First Out manner

# queue operation
# 1: Enqueue: add an item to the queue
# 2: Dequeue: remove item from the list
# 3: Front: Get the front item from the queue
# 4: Rear: Get the last item from the queue

l=[]
while True:
    c=int(input('''
    1 Push element
    2 Pop first element
    3 Front element
    4 Last element
    5 Display Operation
    6 Exit
    '''))
    if c==1:
        n=int(input("Enter the value: "))
        l.append(n)
        print(l)
    elif c==2:
        if(len(l)==0):
            print("Empty queue")
        else:
            del l[0]
            print(l)
    elif c==3:
        if(len(l)==0):
            print("Empty queue")
        else:
            print("First element value: ",l[0])
    elif c==4:
        if(len(l)==0):
            print("Empty queue")
        else:
            print("Last element value: ",l[-1])
    elif c==5:
        if(len(l)==0):
            print("Empty queue")
        else:
            print("Display queue ",l)
    elif c==6:
        break;
    else:
        print("Invalid choice ")
        break;
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     14-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

l=[10,20,30,40,50,60]
print(l,type(l))

# Functions to delete the item from the list

# del function

del l[3]  # remove the value at 3 index which is 40
print(l)

# pop() function

print(l.pop(2))  # remove value at given index and return the value
print(l)

# remove() function

l.remove(20)   # remove the given value from the list
print(l)

# clear() function

l.clear()   # clear the list
print(l)


print()


# Function to update item in the list

k=[10,20,30,40,50]
print(k)

print()

k[4]=60
print(k)

# insert()

k.insert(0,5)  # insert element at given index (index,value)
print(k)

# append()

k.append(70)
print(k)
k.append([1,2,3])
print(k)

# extend()

k.extend([1,2,3])
print(k)

# OTHER LIST FUNCTION

# count()

l=[1,2,3,4,2,1,1,7,8]

print(l.count(1))  # count the number of time element appear in the list

# max()
s=["apple","hello","world"]
print(max(l))   # max will return the maximum value from the list
print(max(s))

# min()

print(min(l))   # min will return the minimum value from the the list
print(min(s))

# sort()

l.sort()
print(l)        # sort the list in increasing format

# reverse()

l.reverse()
print(l)        # reverse the list element

# index()

print(l.index(8))  # index will return the index of element






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

# LIST
# List is mutable (changeable)
# List is a collection of datatype
# List is created by using square bracket


l=[1,2,3,4,4,5]
print(type(l))
print(l[4])
l[4]=8
print(l)

# We can also create list inside another list the another list consider as single element

k=[1,2,3,[4,5,6]]
print(k[3])  # give the full list
print(k[3][1])

m=[2,3,"hello",[3,4,5]]
print(m[2])
print(m[-2])

# LIST SLICING

print(m[0:2])
print(m[1:])
j=[1,2,3,4,5,6,7,8,9,10]
print(j[0::2])
print(j[1::2])
print(j[::])
print(j[-1::-1])


# LIST ITERATION

l=[10,20,30,40,50,60]
a=len(l)
for i in range(a):
    print(l[i])

print()

for i in l:
    print(i)

print()

for i in range(a-1,-1,-1):
    print(l[i])

print()

# LIST COMPREHENSION
# List comprehension is an elegant way to define and create lists based on existing lists
# List comprehension is generally more compact and faster than normal function and loops for creating lists
# SYNTAX [expression for item in list]

p=[]
for a in range(1,101):
    p.append(a)
print(p)

print()

n=[m for m in range(1,101)]
print(n)


print()


j=[h for h in range(1,101) if h%2==0]
print(j)

print()

string="Vaibhav"
o=[v for v in string]
print(o)
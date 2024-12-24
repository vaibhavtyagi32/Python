#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     05-03-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# List: List is a versatile and mutable data structure that allows you to store a collection of items.

a=[1,2,3,4,5]
print(a,type(a))


# List indexing

print(a[1])
print(a[3])
print(a[4])
print(a[-1])
print(a[-3])

a[4]=10
print(a)

a.append([9,4,5])
print(a)

a.extend([8,2,9])
print(a)

a.insert(2,30)
print(a)

x=a.pop(0)
print(a)
print(x)

k=[10,20,30,20,50,20]
k.remove(20)
k.remove(20)
k.remove(20)
print(k)

m=[10,20,30,40]
for i in m:
    print(i)
for i in range(0,len(m)):
    print(m[i])

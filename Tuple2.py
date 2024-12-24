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

# Tuple: tuple is just like a list ,but tuple is immutable once created not changed again

t=(1,2,3,4,5)
print(t,type(t))

# Tuple indexing

print(t[0])
print(t[4])
print(t[-1])
print(t[-4])

# Tuple slicing

print(t[0:])
print(t[0:4])
print(t[-1::-1])

# Two ways of accessing tuple item

# 1st is using IN keyword
l=(10,20,30,"hello")
for i in range(len(l)):
    print(l[i])

for i in l:
    print(i)

# Tuple unpacking

h=(10,20,30)
a,b,c=h
print(b)
print(a)
print(c)

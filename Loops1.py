#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     13-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# LOOPS

range(5)    #(0,1,2,3,4)
# start=0
# condition<5
# increment 1


range(1,6)   #(1,2,3,4,5)
# start=1
# condition<6
# increment 1


range(1,6,2)   #(1,3,5)
# start=1
# condition<6
# increment 2


range(10,0,-1)   #(10,9,8,7,6,5,4,3,2,1)
# start=10
# condition<0
# decrement -1

# FOR LOOP

print("Numbers between 1 to 10 are: ")
for i in range(1,11):
    print(i)



print()



print("odd numbers between 1 to 10 are: ")
for i in range(1,11,2):
    print(i)


print()


print("Table of a number: ")
a=5
for i in range(1,11):
    print(a," * ",i," = "," ",a*i)


print()



print("printing number between 10 to 1 are: ")
for i in range(10,0,-1):
    print(i)


# WHILE LOOPS


i=1
while i<=10:
    print(i)
    i=i+1



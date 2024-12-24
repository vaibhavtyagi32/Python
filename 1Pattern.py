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

for i in range(1,6):
    print(i*"*")

print()

a=1
while a<=5:
    print(a*"*")
    a=a+1

print()


a=int(input("Enter number of rows: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()





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

for i in range(1,6,2):
    print(i*"*")


print()


a=int(input("Enter number of rows: "))
k=1
for i in range(1,a+1):
    for j in range(1,k+1):
        print("*",end=" ")
    k=k+2
    print()

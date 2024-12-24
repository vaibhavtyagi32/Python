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

n=input("Enter a value")

print(n)
l=n.split()  # split() can split the string when space is occur
print(l)

# alternate method

l=[]
for i in range(3):
    n=input("Enter the values "+str(i)+" :-")
    l.append(n)
print(l)
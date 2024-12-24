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

l=[10,20,30,40]
l1=[3,4,77,88,6,17]

# zip() is used to iterate more thn one List at the same time

for a,b in zip(l,l1):
    print(a,b)     #  if both list contain different no of element than it will take element equal to the list having minimum element and igonre the rest element

print()

# other method

t=len(l)
for i in range(t):
    print(l[i],l1[i])




#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     18-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Tuple

# ordered datatype
# created using()
# immutable

t=(20,30,40,50)
print(t,type(t))
a=t[2]
print(a)

l=len(t)
for i in range(l):
    print(t[i])

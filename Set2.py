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

# Set :- set is a collection of  item but the items must be unique and it is unorder and unchanged.
# set is created using {}.

s={1,2,3,4,4,4,4,5}
print(s,type(s))

# we can create set using set() function also

l=[10,20,"hello"]
s=set(l)
print(s)

# Reading is simliar to list but you cannot read it with using indexing because there is no indexing in set

p={10,20,30}
for i in p:
    print(i)
for i in range(len(p)):
    print(p[i])

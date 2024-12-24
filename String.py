#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     10-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

name="Tony Stark"

print(name.upper())
print(name)
# the method can not chagne the original string

print(name.lower())
print(name.find('S'))
# indexing of string is starting with 0th indexes
print(name.find("Stark"))
print(name.replace("Tony Stark","Iron man"))
print(name)
print(name.replace("S","F"))
print(name.capitalize())

a="hello"
b="tony"
c=93
print(a+" "+b)
# print(a+c)
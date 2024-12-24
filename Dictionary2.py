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

# Dictionary

d={1:"vaibhav",2:"harsh",3:"uday"}
e={7:10,8:632,9:736}

print(d,type(d))

d[4]="amit"
print(d)

a=d.keys()
print(a)

b=d.get(2)
print(b)

print(d.items())

d.update(e)
print(d)


for i in d:
    print(d[i])

for i in d.values():
    print(i)

for i in d.keys():
    print(i)

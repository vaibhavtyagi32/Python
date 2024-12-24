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

d={'Name':'Python','Fees':8000,'Duration':'2 months'}

# get()

n=d.get('Name')
print(n)

# keys()

for i in d.keys():
    print(i)
print()

# value()

for j in d.values():
    print(j)
print()

# items

for t in d.items():
    print(t)
print()

# deleting functions

# 1 del()

del d['Fees']
print(d)

# 2 pop()

a=d.pop('Name')
print(a)
print(d)

# dict()

g=dict(name='python',fees=8000)
print(g)

# update()

g.update({'fees':10000})
print(g)

# clear()

g.clear()
print(g)
print()

d['course']="Java"
d['Fees']=8000
d['Duration']='2 months'
print(d)
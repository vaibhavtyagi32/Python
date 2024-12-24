#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     11-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# List:- List is a collection of datatype And List is Muteable
marks=[95,83,93]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[-1])
print(marks[-2])
print(marks[-3])
# print(marks[-4]) (List index out of bound)
print(marks[0:2]) # index 0 and 1 is include
# FOR LOOP IN LIST
for score in marks:
    print(score)
# OPERATION OF LIST
marks.append(99)
print(marks)
marks.insert(2, 56)
print(marks)
print(98 in marks)
print(len(marks))

# WHILE LOOP IN LIST

k=0
while k<len(marks):
    print(marks[k])
    k=k+1
marks.clear()
print(marks)
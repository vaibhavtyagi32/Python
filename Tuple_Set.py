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

# TUPLE IS IMMUTABLE
marks=(87,42,91,42,87)
person="ram","shyam","hello"
print(person)
# marks[1]=76
print(marks.count(42))
print(marks.index(91))

# SET
mark={94,82,82,82,27,92}
print(mark) # REMOVE DUPLICATE ITEM FROM THE SET
# print(mark[0])  Error indexing is not possible in set because item should be place in any location
# Set is Unoreder

# DICTIONARY
hello={"english":85,"maths":63}
print(hello["maths"])
hello["physics"]=92
print(hello)
marks["english"]=96
print(hello)
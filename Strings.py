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

# String:- String is a sequence of character
# String can be created by enclosing charcter inside a single quote or double quote
# triple quote can be used to represent multiline strings
# string indexing start from o from left to right and start from -1 from right to left



v="Hello Vaibhav"
print(v[4])
print(v[6])

# String slicing
print(v[0:6]) # 0 is included but 6 is not included
print(v[0:])  # if we not write the end value it will take rest whole string
print(v[0:6:2])
print(v[0::2])
print(v[-1::-2])
print(v[-1:-10:-2])

# reverse string
print(v[-1::-1])

# string iteration

w="hello vaibhav tyagi"
t=len(w)  # find length of string
for i in range(t):
    print(w[i],end="")


print()

for j in range(t-1,-1,-1):
    print(w[j],end="")

print()

for i in w:
    print(i,end="")
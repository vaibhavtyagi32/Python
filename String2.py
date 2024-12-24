#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     04-03-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Strings: String is a sequence of characters .String are immutable means once created cannot changed agian.
# Strings are created using double quotes ,single quotes, and triple quotes.

n="vaibhav"
print(n,type(n))

# String indexing : String indexing is used to accessed the individual charcter of the strings

print(n[0])
print(n[5])
print(n[6])
print(n[-1])
print(n[-4])


# String slicing : String slicing method is used to access a range of charcter from the string.
# string slicing is done using slicing operator that is colon(:)

print(n[0:3])
print(n[0:])
print(n[0::2])
print(n[-1::-1])

# len(): the len() function is used to calculate the length of the string

print(len(n))

# Two ways of iterating the string

# 1st is by using 'in' keyword

print("Using In Keyword")
for i in n:
    print(i)

# 2nd is by using range function

print("Using Range Function")
for i in range(0,len(n)):
    print(n[i])

# String method

# capitalize() : convert first letters into uppercase

print(n.capitalize())

# upper() : convert all letters into uppercase

print(n.upper())

# lower() : conert all letters into lowercase

k="HELLO"
print(k.lower())

# count() : return a value the number of time character present in the string

print(n.count("v"))
print(n.count("b"))



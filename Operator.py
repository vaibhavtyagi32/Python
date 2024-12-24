#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     12-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# ARTHIMETIC OPERATIONS

a=10
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

# ASSIGNMENT OPERATOR

x=20
print(x)
x=25
print(x)
x += 10
print(x)
x -= 10
print(x)
x *= 2
print(x)
x /= 2
print(x)

# COMAPRISON OPERATOR

p=10
q=20

print(p==q)
print(p!=q)
print(p<q)
print(p>q)
print(p<=q)
print(p>=q)

# LOGICAL OPERATOR

a=10
b=20
print(a==10 and a<b)
print(a==10 or a>b)
print(a!=10)

# MEMBERSHIP OPERATOR  {in ,, not in}

string1="Hello"
print('h' in string1) # PYTHON IS A CASE SENSITIVE LANGUAGE
print('H' in string1)

l=[10,40,73,12,83]
print(50 in l)
print(50 not in l)

#IDENTITY OPERATOR  {is ,, is not}

a=10
b=10
print(a is b,a==b)
print(a is not b,a!=b)

# BITWISE OPERATOR

a=10
b=8

print(bin(10))
print(bin(8))
print(a&b,bin(a&b))

print(a|b,bin(a|b))
print(a^b,bin(a^b))

print(bin(a<<2))
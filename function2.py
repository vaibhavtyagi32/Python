#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     03-03-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Function :- is a reusable block of code that are to perform some task

# Normal parameter

def sum(a,b):
    print("sum is :",a+b)
sum(10,20)
sum(20,30)

# Default parameter

def sum(a,b,c=30):
    print("sum is :",a+b+c)
sum(10,20)
sum(10,20,40)

#Default Argument

def print1(a,b,c):
    print(a)
    print(b)
    print(c)

print1(1,2,3)

# Keyword Argument

def print1(a,b,c):
    print(a)
    print(b)
    print(c)

print1(b=1,c=2,a=3)

# Even odd program

def evenodd(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
evenodd(10)
evenodd(11)

# Function using return statement

def evenodd(a):
    if a%2==0:
        return("even")
    else:
        return("odd")
a=evenodd(13)
print(a)

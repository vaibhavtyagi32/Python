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

w="Hello Vaibhav Tyagi"
n=w.lower()  # convert string into lowercase letter
print(n)
m=w.upper()  # convert string into uppercase letter
print(m)
o=w.capitalize()   # convert the 1st letter into capital letter rest all into lower case letter
print(o)
q=w.title()  # convert the all first letter of word capital
print(q)

print(w.find('el'))   # find function is used to find the subtring in a given string
print(w.find('a',8))   # we can also give the starting index
print(w.find('z'))    # if substring is not found in string it return -1


print(w.index('i'))
# print(w.index('z'))  # if substring is not found in string it return error

t="welcome"
print(t.isalpha())  # It give true if string contains only alphabets otherwise false

k="123"
print(k.isdigit())   # It give true if string contains only digits otherwise false

f="welcome123"
print(f.isalnum())   # It give true if string contains alphabets or digits only7u otherwise false


# CHR() FUNCTION
# This takes in an integer i and convert it to a character c,so it return a character string

y=chr(65)
print(y,type(y))

# ORD() FUNCTION
# This takes a single unicode character(string of length l) and return an integer

y=ord('A')
print(y,type(y))


# FORMAT() FUNCTION
# The format() method formats the specified value(s) and insert them inside the strings placeholder
# The placeholder is defined using curly brackets {}.

# named indexes
txt1="Welcome {fname} {lname}".format(fname="Vaibhav",lname="Tyagi")
print(txt1)

# numbered indexes
txt2="Welcome {0} {1} {2}".format("Vaibhav","Tyagi","Welcome")
print(txt2)

#empty placeholder
txt3="Welcome {} {}".format("Vaibhav","Tyagi")
print(txt3)

# EXAMPLES

o="Welcome {} how are {} your id is {}".format("Vaibhav","You",625)
print(o)

l="Welcome {2} how are {0} your id is {1}".format("Vaibhav","You",625)
print(l)

n="Welcome {a:^10} how are {c:>10} your id is {b:<10}".format(a="Vaibhav",b="You",c=625)
print(n)
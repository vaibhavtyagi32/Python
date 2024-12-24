#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      DELL
#
# Created:     12-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# CONDITIONAL STATEMENT (IF STATEMENT)
a=int(input("Enter a number: "))
if(a%2==0):
    print(a,"Number is Even")
if(a%2!=0):
    print(a,"Number is Odd")

# IF-ELSE STATEMENT

a=int(input("Enter a number: "))
if(a%2==0):
    print(a,"is Even Number")
else:
    print(a,"is Odd Number")

# IF ELIF ELSE STATEMENT
age =65
if(age<13):
    print("you are child")
elif(age<18 and age>13):
    print("you can vote")
else(age>18):
    print("you are adult")
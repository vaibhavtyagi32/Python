#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      DELL
#
# Created:     10-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Select your operation")
print("Press 1 for Addition")
print("Press 2 for Substraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
ch=(input("Enter your choice : "))

def switch(ch):
    if ch=="1":
        print(a+b)
    elif ch=="2":
        print(a-b)
    elif ch=="3":
        print(a*b)
    elif ch=="4":
        print(a/b)
    else:
        print("Invalid choice")
switch(ch)

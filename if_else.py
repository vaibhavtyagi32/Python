#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     10-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

age = int(input("Enter your age ? "))

if age>=18:
    print("You are adult")
    print("You can vote")
elif age>=13 and age<18:
    print("You are teenager")
    print("You are in school")
else:
    print("You are not adult")
    print("You cannot vote")
print("Thankyou")
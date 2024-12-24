#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     21-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#NUMBER GUESSING PROGRAMM

import random as r

userinput=int(input("Enter your number : "))
Computerinput=r.randint(1,100)
print("Computer guess number : ",Computerinput)
if userinput==Computerinput :
    print("Both guess same number")
elif userinput>Computerinput :
    print("Your guess number is too high")
else:
    print("Your guess number is too low")
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     09-03-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# OBJECT ORIENTED PROGRAMMING IN PYTHON

class Factory:
    a=10
    b=20
obj=Factory()
print(obj.a)

class hello:
    def __init__(self):
        print("constructor")
hello()

class factory():
    def __init__(self,BT,tyre,ET):
        self.BT=BT
        self.tyre=tyre
        self.ET=ET
    def showdetails(self):
        print(f"Your details are\n{self.BT}\n{self.tyre}\n{self.ET}")
ferrari=factory("covered",4,"8 cycle")
print(ferrari.BT)
alto=factory("covered",4,"4 cycle")
print(alto.ET)
alto.showdetails()


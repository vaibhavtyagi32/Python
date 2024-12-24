#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     19-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def hello():
    print("Hello vaibhav")
print("Executing function")
hello()

def hello1(name,ending):
    print("Hello"+name)
    print(ending)
print("Executing function")
hello1('vaibhav','thankyou')
print("Done")

def lettergenerator(name,date):
    st= f"Hey mam, This is {name} and I will not able to attend college on {date}"
    print(st)
lettergenerator("vaibhav","29 Feb")
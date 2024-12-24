#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     18-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Nested Dictionray

# nested dictionary means putting a dictionary inside another dictionary
# it is a collection of dictionary into one single dictionary

course={'php':{'duration':'2 months','fees':10000},
        'java':{'duration':'2 months','fees':10000},
        'python':{'duration':'2 months','fees':10000}
        }
print(course)
print(course['php'])
print(course['php']['fees'])

for i,j in course.items():
    print(i,j['duration'],j['fees'])


#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     11-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

students=["ram","shyam","kishan","radha","radhika"]
for i in students:
    if(i=="radha"):
        break;
    print(i)
for j in students:
    if(j=="kishan"):
        continue;
    print(j)
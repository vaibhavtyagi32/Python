#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     22-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pickle
l=[1,2,3,4,5]
file1=open("text.txt","wb")
pickle.dump(l,file1)
file1.close()
file1=open("text.txt","rb")
l1=pickle.load(file1)
print(l1[0:4])
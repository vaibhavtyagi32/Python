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

import json
d={
    'course_name':'python',
    'fee':8000
}
f=json.dumps(d)
print(f,type(f))
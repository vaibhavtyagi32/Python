#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     06-03-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# String questions

# 1Q: PRINT STRING IN REVERSE ,ITS LENGTH,TO UPPERCASE, TO LOWERCASE,COPY INTO
# OTHER STRING.

s="Vaibhav Tyagi"
r=""
print(s[-1::-1])
for i in range(len(s)-1,-1,-1):
    r=r+s[i]
print(r)
print(len(s))
print(s.lower())
print(s.upper())
c=s
print(c)

# 2Q: ARRANGE STRING CHARACTER SUCH THAT LOWERCASE LETTER COME FIRST IN OTHER STRING.

a="vaiBHav tyAgI"
b=""

for i in a:
    if i.islower():
        b=b+i
for i in a:
    if i.isupper():
        b=b+i
print(b)

# 3Q: COUNT ALL LETTERS ,CHAR, SPECIAL SYMBOL IN A STRING

J="jhjsks51749@#$43"
char=0
digit=0
symbol=0
for i in J:
    if i.isalpha():
        char=char+1
    if i.isdigit():
        digit=digit+1
    else:
        symbol=symbol+1


print(f"your counting are \nnumbers = {digit} \ncharacter = {char} \nsymbol = {symbol}")

# 4Q: COUNTING VOWEL OF THE GIVEN STRING

f="vaibhavTYAGI"
count=0
for k in "aeiouAEIOU":
        count=count+1
print("Number of vowels are : ",count)


#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     29-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Loops Questions

#Print natural number upto n


n=int(input("Enter any number : "))
for i in range(1,n+1):
    print(i)


# Reverse for loop to print n to 1


m=int(input("Enter any number : "))
for i in range(m,0,-1):
    print(i)


# Table of any numbers


a=int(input("Enter any number : "))
for i in range(1,11):
    print(a," * ",i," = ",a*i)

# sum upto n terms


s=int(input("Enter any number : "))
k=0
for s in range(1,s+1):
    k=k+s
print("sum is : ",k)


#Factorial of a number


m=int(input("Enter any number : "))
t=1
for i in range(m,0,-1):
    t=t*i
print("Factorial is ",t)


#Factors of a number


m=int(input("Enter any number : "))
for i in range(1,m+1):
    if m%i==0:
        print(i)


# Perfect number or not


m=int(input("Enter any number : "))
s=0
for i in range(1,m):
    if m%i==0:
        s=s+i
if(s==m):
    print(m," is Perfect number")
else:
    print(m,"is not a perfect number")


# Number is prime or not


m=int(input("Enter any number : "))
t=0
for i in range(2,m):
    if(m%i==0):
        t=1
        break;
if t==0:
    print(m," is a prime number")
else:
    print(m," is not a prime number")


# Seprate each digit of a number and print in new line


a=int(input("Enter any number : "))
while a>0:
    r=0
    r=a%10
    print(r,end=" ")
    a=a//10


print()
# Numbers is palindrome or not

m=int(input("Enter any number : "))

r=0
t=m
while m>0:
    k=m%10
    r=r*10 + k
    m=m//10
if t==r:
    print("Palindrome")
else:
    print("Not Plaindrome")



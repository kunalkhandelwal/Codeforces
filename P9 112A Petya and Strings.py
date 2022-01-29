# -*- coding: utf-8 -*-
"""
Created on Sun May 16 17:46:30 2021

@author: Kunal
"""

str1=str(input(""))
str2=str(input(""))

s1= str1.lower()
s2= str2.lower()

l1=s1.split()#we are splitting the strings and storing them in a list so that we can sort them alphabetically
l2=s2.split()
#print(s1,s2)
l1.sort()
l2.sort()

if l1>l2:
    print(1)
elif l2>l1:
    print(-1)
else:
    print(0)        

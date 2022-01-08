# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 03:03:41 2021

@author: Kunal Khandelwal
"""
l=[]
for i in range(3):
    l.append(int(input()))
#print(l)
a=l[0]
b=l[1]
c=l[2]

e1=a+b+c
e2=a*b*c
e3=(a+b)*c
e4=a*(b+c)
e5=a+(b*c)
e6=(a*b)+c

l1=[e1,e2,e3,e4,e5,e6]
l1.sort()
print(l1[-1])
    

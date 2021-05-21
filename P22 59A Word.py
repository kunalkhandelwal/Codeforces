# -*- coding: utf-8 -*-
"""
Created on Fri May 21 23:06:38 2021

@author: kkhan
"""

s=str(input(""))
length=len(s)
c1=c2=0
upper ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower='abcdefghijklmnopqrstuvwxyz'

for i in range(length):
    if s[i] in upper:
        c1=c1+1
    else:
        c2=c2+1
    length-=1
    
if c1<=c2:
    print(s.lower())
else:
    print(s.upper())
    
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 12:56:12 2021

@author: Kunal Khandelwal
"""
n1=str(input())
n2=str(input())
s=''
#print(n1,n2)

for i in range(len(n1)):
    if n1[i]!=n2[i]:
        s=s+'1'
    else:
        s=s+'0'
print(s)
        

# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 22:15:54 2021

@author: kkhan
"""

a=set(str(input("")))
k1=list(a)
#print(k1)
count=0
for i in range(len(k1)):
    if k1[i]==',' or k1[i]=='{' or k1[i]=='}' or k1[i]==' ':
        count=count+1
if len(a)>0:
    print(len(a)-count)
else:
    print(0)
        
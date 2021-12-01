# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 13:04:10 2021

@author: Kunal
"""

n=int(input())
a=list(map(int, input().split()))
vol=0
x=1
total=n*x
for i in range(len(a)):
    k=(a[i]/100)*x
    vol=vol+k
print((vol/total)*100)
    

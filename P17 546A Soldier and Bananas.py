# -*- coding: utf-8 -*-
"""
Created on Thu May 20 01:55:52 2021

@author: Kunal
"""

k,n,w =map(int, input().split())
#print(k,n,w)
count=k1=0
for i in range(1,w+1):
        k1=k*i
        count=count+k1
if count>n:
    print(count-n)
else:
    print(0)
    

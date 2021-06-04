# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:58:15 2021

@author: kkhan
"""

n,m=list(map(int, input().split()))
f=list(map(int, input().split()))

f.sort()
temp=99999999
for i in range(m-n+1):
    #print(i)
    diff=f[i+n-1]-f[i]    
    if temp>diff:
        temp=diff    
print(temp)
    
    
    
    

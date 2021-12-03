# -*- coding: utf-8 -*-
"""
Created on Sat May 15 21:33:47 2021

@author: Kunal
"""

b = list(map(int, input().split()))
n=b[0]
k=b[1]
    
a= list(map(int, input().split()))
#print(a)
cnt=0
for i in range(len(a)):
    if a[i]>0:
        if a[i]>=a[k-1]:
            cnt+=1
    
print(cnt)
    
    


# -*- coding: utf-8 -*-
"""
Created on Sat May 29 22:40:59 2021

@author:Kunal
"""
n=int(input())
#arr=list(map(int, input().split()))
#print(arr)
a=[]
count=0
for i in range(n):
    a.append(str(input()))
#print(a)
for i in range(1,n):
    if a[i-1]!=a[i]:
        count=count+1
print(count+1) 

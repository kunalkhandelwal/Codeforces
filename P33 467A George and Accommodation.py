# -*- coding: utf-8 -*-
"""
Created on Fri May 28 00:08:52 2021

@author: kkhan
"""
n=int(input())
cnt=0
for i in range(0,n):
    p,q=list(map(int, input().split()))
    #print(p,q)
    if q-p>=2:
        cnt=cnt+1
        #print(cnt)
    else:
        cnt=cnt+0
        #print(cnt)
print(cnt)

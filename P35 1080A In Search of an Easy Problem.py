# -*- coding: utf-8 -*-
"""
Created on Sat May 29 18:15:23 2021

@author: Kunal
"""

n=int(input())
a=list(map(int, input().split()))
#print(a)
cnt1=0
for i in range(n):
    if 1 in a:
        cnt1=cnt1+1
        #print(cnt1)
if cnt1>0:
    print("HARD")
else:
    print("EASY")

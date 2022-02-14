# -*- coding: utf-8 -*-
"""
Created on Mon May 31 02:09:24 2021

@author: Kunal Khandelwal
"""
#https://codeforces.com/problemset/problem/580/A

n=int(input())
a=list(map(int, input().split()))
cnt1=1
ans=1
l=[]
for i in range(1,n):
    if a[i-1]<=a[i]:
        cnt1=cnt1+1
        l.append(i)
    else:
        cnt1=1
    ans=max(ans,cnt1)
        #print(i)
print(ans)
    

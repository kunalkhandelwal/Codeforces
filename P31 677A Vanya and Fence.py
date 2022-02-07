# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:02:23 2021

@author: Kunal Khandelwal
"""

n,h=list(map(int, input().split()))
arr=list(map(int, input().split()))
#print(n,h,arr)
cnt=0
for i in range(0,n):
    if arr[i]>h:
        cnt=cnt+2
    else:
        cnt=cnt+1
print(cnt)

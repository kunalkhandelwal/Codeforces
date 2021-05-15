# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:58:26 2021

@author: Kunal
"""
n=int(input(""))
cnt=0
for i in range(n):
    arr = list(map(int, input().split()))
    if arr[0] and arr[1]==1 or arr[1] and arr[2]==1 or arr[2] and arr[0]==1:
            cnt=cnt+1
print(cnt)
    #else:
            #print(cnt)
            #print("\n")
"""
cnt=0
if arr[0] and arr[1]==1 or arr[1] and arr[2]==1 or arr[2] and arr[0]==1:
    cnt=cnt+1
    print(cnt)
else:
    print(cnt)
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 07:45:00 2021

@author: kkhan
"""

n=int(input(""))
a=list(map(int, input().split()))
maxx=0
minn=101
for i in range(n):
    if a[i]>maxx:
        maxx=a[i]
        index_max=i
    if a[i]<=minn:
        minn=a[i]
        index_min=i
n=n-1
if index_max>index_min:
    index_min= index_min +1
print(index_max+ n- index_min)
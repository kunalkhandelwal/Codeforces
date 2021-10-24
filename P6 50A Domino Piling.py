# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:57:25 2021

@author: Kunal
"""

a=list(map(int, input().split()))
m = a[0]
n = a[1]

area= m*n
if area%2==0:
    print(int(area/2))
else:
    print(area//2)


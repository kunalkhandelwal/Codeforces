# -*- coding: utf-8 -*-
"""
Created on Thu May 20 03:18:16 2021

@author: kkhan
"""

n,k =map(int, input().split())
for i in range(k):
    if n%10==0:
        n=int(n/10)
    else:
        n=n-1
print(n)
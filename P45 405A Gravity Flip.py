# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 03:16:54 2021

@author: kkhan
"""

n=int(input())
a=list(map(int, input().split()))

a.sort()

for i in range(n):
    print(a[i], end=" ")
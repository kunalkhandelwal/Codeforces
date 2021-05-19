# -*- coding: utf-8 -*-
"""
Created on Thu May 20 02:28:39 2021

@author: kkhan
"""

a,b=map(int, input().split())
for i in range(1,7):
    a=a*3
    b=b*2
    if a>b:
        print(i)
        break

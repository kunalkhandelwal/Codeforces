# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 07:38:59 2021

@author: kkhan
"""

n=int(input(""))
cnt=0
if n%100>=0:
    #cnt=cnt+1
    cnt=n//100
    n=n%100
if n%20>=0:
    #cnt=cnt+1
    cnt=cnt+n//20
    n=n%20
if n%10>=0:
    #cnt=cnt+1
    cnt=cnt+n//10
    n=n%10
if n%5>=0:
    #cnt=cnt+1
    cnt=cnt+n//5
    n=n%5
if n%1>=0:
    #cnt=cnt+1
    cnt=cnt+n//1
print(cnt)
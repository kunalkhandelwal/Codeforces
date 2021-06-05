# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 03:43:24 2021

@author: kkhan
"""

n=int(input(""))
count=0
l=[]
while(n):
    a,b=list(map(int, input().split()))
    #print(a,b)
    if a%b==0:
        print(0)
    else:
        print(b-a%b)
    n=n-1
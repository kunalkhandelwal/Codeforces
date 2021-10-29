# -*- coding: utf-8 -*-
"""
Created on Fri May 21 02:45:05 2021

@author: Kunal Khandelwal
"""

n=int(input(""))
s=m=0
while n:
     a,b=map(int,input().split())
     s=s+b-a
     if s>m :
         m=s
     n=n-1
print(m)
    
     


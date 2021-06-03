# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:51:32 2021

@author: kkhan
"""

k=int(input(""))
l=int(input(""))
m=int(input(""))
n=int(input(""))
d=int(input(""))
cnt=0
for i in range(1,d+1): 
    #print(i)
    if i%k==0:
        cnt=cnt+1
        #print(cnt)
    elif i%l==0 :
        cnt=cnt+1
       # print(cnt)
    elif i%m==0:
        cnt=cnt+1
        #print(cnt)
    elif i%n==0:
        cnt=cnt+1
        #print(cnt)
if k>d and l>d and m>d and n>d:
    print(0)
else:
    print(cnt)
    
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:07:20 2021

@author: kkhan
"""

n=int(input(""))
h=[]
g=[]
count=0
for i in range(n):
    home,guest=list(map(int, input().split()))
    h.append(home)
    g.append(guest)
#print(h,g)
    
for i in range(n):
    for j in range(n):
        if h[i]==g[j]:
            count=count+1
print(count)

        
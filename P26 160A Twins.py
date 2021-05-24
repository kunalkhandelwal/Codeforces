# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:00:54 2021

@author: kkhan
"""
n=int(input(""))
a=list(map(int, input().split()))
#print(l)

a.sort()
#l.reverse()
#print(l)

s=c=cnt=0
for i in a:
    s=s+i
for i in a[::-1]:
    c=c+i
    cnt=cnt+1
    if c>(s/2):
        break
print(cnt)
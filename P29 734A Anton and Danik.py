# -*- coding: utf-8 -*-
"""
Created on Wed May 26 02:00:27 2021

@author: Kunal
"""

n=int(input(""))
s=str(input(""))

cnt1=cnt2=0
for i in s:
    if 'D' in i:
        cnt1=cnt1+1
    if 'A' in i:
        cnt2+=1
#print(cnt1, cnt2)
if cnt1>cnt2:
    print("Danik")
elif cnt2>cnt1:
    print("Anton")
else:
    print("Friendship")

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 07:02:30 2021

@author: kkhan
"""

n=int(input(""))
a=str(input(""))
a1=a.lower()
s=[]
s=set(s)
#print(a1)

for i in range(n):
    if ord(a1[i])>=97 and ord(a1[i])<=122:
        s.add(ord(a1[i]))
#print(s)
'''
if cnt>=26:
    print("YES")
else:
    print("NO")
 '''
if len(s)==26:
    print("YES")
else:
    print('NO')       
# -*- coding: utf-8 -*-
"""
@author: Kunal
"""


arr = list(map(int, input().split()))

n=arr[0]
m=arr[1]
a=arr[2]

cnt1= n//a
#print(cnt1)
if n%a!=0:
    cnt1=cnt1+1
cnt2=m//a
#print(cnt2)
if m%a!=0:
    cnt2=cnt2+1
print(cnt1*cnt2)
    





'''
m=int(input("\n"))
a=int(input("\n"))
a1=n*m
a2=a*a
print(a1/a2)
'''
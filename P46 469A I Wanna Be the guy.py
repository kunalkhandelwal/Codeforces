# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 03:27:31 2021

@author: Kunal
"""

n=int(input())
x=list(map(int, input().split()))
y=list(map(int, input().split()))
x.pop(0)
y.pop(0)
s=x+y
#print(s)
s=set(s)
s.discard(0)
#print(s)

if len(s)==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

'''
cnt1=cnt2=cnt3=cnt4=0
for i in range(len(x)):
    if x[i]==n:
        cnt1=cnt1+1
        break
    
for i in range(len(y)):
    if y[i]==n:
        cnt2=cnt2+1
        break
    
for i in range(n):
    if x[i]==i:
        cnt3=cnt3+1
    elif y[i]==i:
        cnt4=cnt4+1
    
    
   
if cnt1==0 and cnt2==0:
    print("Oh, my keyboard!")   
elif cnt3+cnt4<n:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")
    
'''
'''
n=int(input())
x=list(map(int, input().split()))
y=list(map(int, input().split()))
cnt1=cnt2=0
for i in range(len(x)):
    if x[i]==n:
        cnt1=cnt1+1
        break
    #print("Oh, my keyboard!")
for i in range(len(y)):
    if y[i]==n:
        cnt2=cnt2+1
        break
    #print("Oh, my keyboard!")
if cnt1==0 and cnt2==0:
    print("Oh, my keyboard!")   
else:
    print("I become the guy.")
'''

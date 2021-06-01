# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:30:45 2021

@author: kkhan
"""
#https://codeforces.com/problemset/problem/486/A
n=int(input())
if n%2==0:
    print(int(n/2))
else:
    print(int(-(n+1)/2))
'''
n=int(input())
def func():
    op=0
    for i in range(1,n+1):
        #print((-1)**i)
        k=((-1)**i)*i
        op=op+k
    print(op)
func()

 Time limit exceeded in test case 3=1000000000
'''





   
     

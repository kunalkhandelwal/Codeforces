# -*- coding: utf-8 -*-
"""
Created on Sun May 31 01:13:09 2021

@author: kkhan
"""

n,k=list(map(int, input().split()))
odd, even = (n+1)//2, n//2
#print(odd,even)   
if k<=odd:
    print(int((2*k) - 1))
else:
    print(int((k-odd)*2 ))

'''
FIRST I CODED THIS, but the time limit exceeded in the 8th test case
n,k=list(map(int, input().split()))
l=[]
for i in range(1,n+1):    
    if i%2==1:
        l.append(i)
        #print(l)
        
for i in range(1,n+1):    
    if i%2==0:
        l.append(i)
        #print(l)
print(l[k-1])    
'''  
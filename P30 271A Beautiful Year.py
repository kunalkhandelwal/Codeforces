# -*- coding: utf-8 -*-
"""
Created on Wed May 26 02:33:54 2021

@author: kkhan
"""

n=int(input())
temp=n
#n=n+1
#print(k)

k=0

while(k>=0):
    temp=temp+1  
    n=temp+1
    n1=n%10
    n=n//10
    n2=n%10
    n=n//10
    n3=n%10
    n=n//10
    n4=n%10
    k=k+1
    #print(temp)
    #print(n4, n3, n2 ,n1)
    if(n1!=n2 and n1!=n3 and n1!=n4 and n2!=n3 and n2!=n4 and n3!=n4):
        print(temp)
        break
        
    
    
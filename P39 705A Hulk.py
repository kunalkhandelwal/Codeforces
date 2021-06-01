# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 02:37:02 2021

@author: kkhan
"""

n=int(input())
if n%2==0:
    n1=n//2
    n2=n//2
    p1=n1*("I hate that I love that ")
    p1=p1[:-5]+'it'
    print(p1)
else:
    n2=n//2
    n1=n-n2
    #print(n1)   
    p2=(n2*"I hate that I love that " + "I hate it")
    print(p2)
    
        
        
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 03:25:34 2021

@author: Kunal
"""

x=int(input(""))
count=0
while x>=5:
        count=x//5
        x=x%5
        #print(count)
if x%4==0:
    count=count + x//4
    #print(count)
    x=x%4
elif x%3==0:
    count= count + x//3
    #print(count)
    x=x%3
elif x%2==0:
    count=count + x//2
    #print(count)
    x=x%2
else:
    count=count + x//1
    #print(count)
print(count) 


"""
DISCARDED CODE

This was my earlier approach to solve the problem
x=int(input(""))
count=0
if x%5!=0:
    count=count + x//5
    x=x%5
elif x%4!=0:
    count=count + x//4
    x=x%4
elif x%3!=0:
    count= count + x//3
    x=x%3
elif x%2!=0:
    count=count + x//2
    x=x%2
else:
    count=count + x//1
print(count)
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 17 18:45:29 2021

@author: kkhan
"""


s=input("")
n1=n2=n3=0

for i in range(0,len(s),2):
    if s[i]=="1":
        n1+=1
    elif s[i]=="2":
        n2+=1
    else:
        n3+=1
        
ans="1+"*n1 + "2+"*n2 + "3+"*n3
print(ans[:-1])
    
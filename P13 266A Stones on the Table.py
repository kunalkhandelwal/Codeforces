# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:42:31 2021

@author: Kunal
"""
n=int(input(""))
s=str(input(""))

#print(n)
#print(s)
R=G=B=0

for i in range(1,n):
        if s[i-1]==s[i]:
            if s[i]=="R":
                R+=1
            elif s[i]=="G":
                G+=1
            else:
                B+=1
                
print(R+G+B)
        

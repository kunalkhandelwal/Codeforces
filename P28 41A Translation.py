# -*- coding: utf-8 -*-
"""
Created on Wed May 26 01:25:58 2021

@author: Kunal Khandelwal
"""

s=str(input(""))
t=str(input(""))
i=k=0
#t.reverse() STRING CANNOT BE REVERSED HENCE THIS IS NOT DONE if input is in STRING FORM
def reverse():
    string=''
    for i in s:
        string=i+string
    return string
#print(reverse())

if t==reverse():
    print("YES")
else:
    print("NO")

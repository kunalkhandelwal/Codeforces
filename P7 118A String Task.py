# -*- coding: utf-8 -*-
"""
Created on Sun May 16 02:18:59 2021

@author: Kunal Khandelwal
"""


"""
#The below code Didn't work
#n=str(input(""))
#n1=n.lower()
n1=n.lower()

def fun(n1):
    vowels= ("a","e","i","o","u","y")
    for x in n1:
        if x in vowels:
            n1=n1.replace(x,"")
        else:
            n1=n1.replace(x,"."+x)
        print(n1)
    
fun(n1)
 """       
n=str(input(""))
n1=n.lower()  
s=""
vowels= ("a","e","i","o","u","y")
for i in range(0, len(n1)):
    if n1[i] not in vowels:
        s=s+"."
        s=s+n1[i]
print(s)

         

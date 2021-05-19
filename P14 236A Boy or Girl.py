# -*- coding: utf-8 -*-
"""
Created on Wed May 19 11:53:13 2021

@author: Kunal
"""
n=str(input(""))
#print(n)
count=0
string=""

#    #for j in range(i+1,len(n)):
#        if n[i]==n[j]:
##            if n[i] not in string:
##                string=string+n[i]
#            count=count+1
for i in range(0,len(n)):
    if n[i] not in string:
        string=string+n[i]
        
count=len(string)
#print(count)
#print(len(n))
if count%2==0:
    print('CHAT WITH HER!')
else:
    print("IGNORE HIM!")
    
"""        
wjmzbmr
CHAT WITH HER!

xiaodao

IGNORE HIM!

sevenkplus

CHAT WITH HER!
pezu
CHAT WITH HER!

zcinitufxoldnokacdvtmdohsfdjepyfioyvclhmujiqwvmudbfjzxjfqqxjmoiyxrfsbvseawwoyynn
IGNORE HIM!
"""        
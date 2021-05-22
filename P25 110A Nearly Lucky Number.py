# -*- coding: utf-8 -*-
"""
Created on Sun May 23 02:26:41 2021

@author: kkhan
"""
n=input("")
l=[]
count=0
if n=='47' or n=='74' or n=='44' or n=='77' or n=='444' or n=='447' or n=='474' or n=='477' or n=='744' or n=='747' or n=='774' or n=='777':
    print("YES")
    
else:
    for i in range(len(n)):
        l.append(n[i])
        #print(l)
        if l[i]=='4':
            count=count+1
        if l[i]=='7':
            count+=1
    #print(count)
    
    if count==4 or count==7:
        print("YES")
    else:
        print("NO")
    

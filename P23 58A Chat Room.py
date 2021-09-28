# -*- coding: utf-8 -*-
"""
Created on Fri May 21 23:25:29 2021

@author: Kunal
"""
s1='hello'
def chatRoom():
    s=str(input())
#print(type(s))=stringof a string.
#Whenever we take input without mentioning the type of input, it is always in thr form 
#print(s)
    
    x=0
    for i in range(len(s)):
        if s[i]==s1[x]:
            x=x+1
        if x==5:
            return "YES"
    return"NO"
print(chatRoom())


'''
My initial approach of solving this question was this, which is not correct.
for i in range(len(s)):
    if 'h' in s:
        count=count+1
        #print(count)
        if 'e' in s:
            count=count+1
            #print(count)
            if 'l' in s:
                count=count+1
                #print(count)
                if 'l' in s:
                    count=count+1
                    #print(count)
                    if 'o' in s:
                        count=count+1
                        print("YES")
                        break
                    else:
                        print("NO")
                        break

if count==5:
    print("YES")
else:
    print("NO")                    
'''
    

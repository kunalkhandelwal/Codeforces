# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:01:51 2021

@author: Kunal Khandelwal
"""

#a=[list(map(str, input().split())) for j in range(n)]
#above line is the way to take input in new line and store every element in the list in the form of list
#a=list(map(str, input().split()))


"""
arr=[]
for i in range(0, n):
    ele = str(input(""))
    arr.append(ele)
#print(a)
"""
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 12:37:54 2021

@author: Kunal
"""

n=int(input(""))
#a=[list(map(str, input().split())) for j in range(n)]
#above line is the way to take input in new line and store every element in the list in the form of list
#a=list(map(str, input().split()))
arr=[]
a=0
for i in range(0, n):
    ele = input("")
    arr.append(ele)
#print(a)
 
for i in range(n):
    if 'X++'== arr[i]:
        a=a+1
        #print(s)
    if 'X--'== arr[i]:
        a=a-1
        #print(s)
    if '++X' == arr[i]:
        a=a+1
        
        #print(s)
    if '--X' == arr[i]:
        a=a-1
        
        #print(s)  
print(a)



"""n=int(input(""))
a=0
arr=list(map(str, input().split()))
for i in range(n):
    if 'x++' in arr:
        x=a
        a=a+1
        #print(s)
    if 'x--' in arr:
        x=a
        a=a-1
        #print(s)
    if '++x' in arr:
        a=a+1
        x=a
        #print(s)
    if '--x' in arr:
        a=a-1
        x=a
        #print(s)
print(x)
"""
    
"""
n=int(input(""))
#a=[list(map(str, input().split())) for j in range(n)]
#above line is the way to take input in new line and store every element in the list in the form of list
a=list(map(str, input().split()))
s=0
#print(a)
for i in range(n):
    if 'x++' in a:
        s=s+1
        #print(s)
    if 'x--' in a:
        s=s-1
        #print(s)
    if '++x' in a:
        s+=1
        #print(s)
    if '--x' in a:
        s-=1
        #print(s)
print(s)
"""

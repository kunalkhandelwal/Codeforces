# -*- coding: utf-8 -*-
"""
Created on Wed May 19 17:28:29 2021

@author: kkhan
"""
x=int(input(''))
sx=sy=sz=0
for i in range(x):
    x,y,z=map(int, input('').split())
    sx=sx+x
    sy+=y
    sz+=z
 
if(sz==sy==sz==0):
    print("YES")
else:
    print("NO")

    


    
"""
n=int(input(""))
arr=0
for i in range(0,n):    
    arr[i]=list(map(int, input().split()))
    
print(arr)
count=0
for i in range(len(arr)):
    count=count+arr[i]
if count==0:
    print("YES")
else:
    print("NO")
"""
#n=int(input(""))
#n1=str(n)
'''v1=list(map(int, input().split()))
v2=list(map(int, input().split()))
v3=list(map(int, input().split()))

#print(n,v1,v2,v3)
count=0
for i in range(0,n):
    k=v1[i]+v2[i]+v3[i]
    print(k)
    count=count+k    
#print(count)
if count==0:
    print("YES")
else:
    print("NO")
    #The above code gave me runtime errors
    '''
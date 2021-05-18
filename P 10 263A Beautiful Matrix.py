# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:55:17 2021

@author: kkhan
"""
matrix=[]

#Below is the code for taking input in a matrix by appending the rows in the form of lists in the matrix

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
    #print(row)
#print(matrix)
m=list(matrix)

for i in range(5):
    for j in range(5):
        if m[i][j]==1:
            i1,i2=i+1,j+1#adding 1 to it because the rows and coloumns both are from 1 to 5
            #print(i1,i2), print and check whether it is giving you right values of rows and coloumns that start from 1 to 5
k1,k2=0,0

if i1<3:
    k1=3-i1
elif i1>3:
    k1=i1-3
else:
    k1=0
    
if i2<3:
    k2=3-i2
elif i2>3:
    k2=i2-3
else:
    k2=0

print(k1+k2)
                

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 07:32:14 2021

@author: kkhan
"""

n=int(input(""))
cnt=0
for i in range(n):
    s=str(input(""))
    if s=='Tetrahedron':
        cnt=cnt+4
    elif s=='Cube':
        cnt=cnt+6
    elif s=='Octahedron':
        cnt=cnt+8
    elif s=='Dodecahedron':
        cnt+=12
    elif s=='Icosahedron':
        cnt+=20
print(cnt)
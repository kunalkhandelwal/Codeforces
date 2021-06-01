# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 13:16:16 2021

@author: kkhan
"""

s=str(input())
s1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if s==s.upper():
    print(s.lower())
elif s==s.capitalize():
    print(s)
elif len(s)==1:
    print(s.upper())
else:
    if (s[0] not in s1) and s[1:].isupper(): 
        print(s.capitalize())
    else:
        print(s)
    
'''

MY INITIAL APPROACH TO SOLVE THE PROBLEM THAT WAS WRONG

s=str(input())
if s==s.upper():
    print(s.capialize())
elif s==s.capitalize():
    print(s)
else:
    s1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s2=''
    for i in range(len(s)):
        if s[i] in s1:
            s2=s2+s[i]
        else: 
            s2=s2+s[i]
    print(s2.capitalize())
    '''
    

    


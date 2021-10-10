# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:11:19 2021

@author: Kunal
"""

p=str(input(""))
#print(len(p))
while(p):
    if 'H' in p:
        print("YES")
        break
    elif 'Q' in p:
        print("YES")
        break
    elif '9' in p:
        print("YES")
        break
#    elif '+' in p:
#        print("YES")
#        break
    else:
        print("NO")
        break    
    
    
'''
I DON'T KNOW WHY WAS THIS CODE GIVING ERROR ON TESTCASE 10: 
    dEHsbM'gS[\brZ_dpjXw8f?L[4E"s4Zc9*(,j:>p$}m7HD[_9nOWQ\uvq2mHWR
for i in range(len(p)):
#while(len(p)):
    if 'H' in p[i]:
        print("YES")
        break
    elif 'Q' in p[i]:
        print("YES")
        break
    elif '9' in p[i]:
        print("YES")
        break
    elif '+' in p[i]:
        print("YES")
        break
    else:
        print("NO")
        break
'''

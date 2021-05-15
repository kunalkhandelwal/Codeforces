# -*- coding: utf-8 -*-
"""

@author: Kunal
"""

n = int(input(""))

for i in range(n):
    s=input("\n")
    if len(s)<=10:
        print(s)
    else:
        ans= s[0]+ str(len(s)-2)+s[-1]
        print(ans)
       
        
'''n = int(input())
for i in range(n):
    s = input()
    ans = s[0] + str(len(s) - 2) + s[-1] if len(s) > 10 else s
    print(ans)'''       
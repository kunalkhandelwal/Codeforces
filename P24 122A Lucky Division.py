# -*- coding: utf-8 -*-
"""
Created on Sat May 22 18:40:07 2021

@author: kkhan
"""
n=int(input(""))
if n==4 or n==7 or n==47 or n==74 or n==44 or n==77 or n==444 or n==447 or n==474 or n==477 or n==744 or n==747 or n==774 or n==777:
    print("YES")
elif n%4==0 or n%7==0 or n%47==0:
    print("YES")
else:
    print("NO")
    
    
    
    
'''
#Below mentioned are my initial approaches for the question which didn't work out.

n=int(input(""))
dig1=0
dig2=0
dig3=0
count=0
if n%4==0 or n%7==0:
            print("YES")

else:            
    while(n!=0):
        dig3=n%10
        n=n//10
        #print(n)
        dig2=n%10
        n=n//10
        #print(n)
        dig1= n%10
        #print(n)
        break
    s=dig1 + dig2+ dig3
    #print(dig1, dig2, dig3)
    if dig1==4 or dig1==7:
        count+=1
    if dig2==4 or dig2==7:
        count+=1
    if dig3==4 or dig3==7:
        count+=1
        
    if count<=3:
        print("YES")
    

if (dig1==4 or dig2==4 or dig3==4) or (dig1==7 or dig2==7 or dig3==7) and (s==4 or s==7 or s==8 or s==14 or s==12 or s==15 or s==18 or s==21):
    print("YES")
else:
    print("NO")
'''
'''
n=input("")
#n=int(n)
a,b='4','7'

for i in range(len(n)):
    if a or b not in n:
        n=int(n)
        if n%4==0 or n%7==0:
            print("YES1")
            break
        else:            
            while n!=0:
                d = n%10
                n = int(n/10)
                if(d%7 == 0):
                    print("YES2")
                    break
                elif(d%4==0):
                    print("YES3")
                    break
                else:
                    print("NO")
'''

    
        
       
g=str(input())
h=str(input())
a=str(input())
g1=h1=a1=[]
g1=list(g)
#print(g1)

h1=list(h)
#print(h1)

a1=list(a)
#print(a1)

k=g1+h1
k.sort()
#print(k)
a1.sort()
#print(a1)

if k==a1:
    print("YES")
else:
    print("NO")


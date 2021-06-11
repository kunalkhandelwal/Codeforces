
n=int(input())
a=i=0
l=[]
for i in range(n):
    l.append(int(input()))
    if l[i]==0 or l[i]==1 or l[i]==2:
        print(0)
    elif l[i]%2!=0:
        print(l[i]//2)
    elif l[i]%2==0:
        print((l[i]//2)-1)
a=list(map(int,input().split()))
n=int(input())
l1=[]
p=0
for i in range(n):
    l=list(map(int,input().split()))
    l1.append(l)
for i in l1:
    c=0
    for j in i:
        if (j in a) and len(a)>len(i):
            c=c+1
        if c==len(i):
            p=p+1    
if p==len(l1):
    print(True)
else:
    print(False)                

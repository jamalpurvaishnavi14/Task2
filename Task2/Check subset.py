t=int(input())
for i in range(t):
    l=[]
    l1=[]
    c=0
    n1=int(input())
    l=list(map(int,input().split()))
    n2=int(input())
    l1=list(map(int,input().split()))
    for i in l:
        if i in l1:
            c=c+1
    if c==len(l):
        print(True)
    else:
        print(False)

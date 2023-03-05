N=int(input()) 
list=[]
for i in range(N):
    sub = input().split()
    if 'insert' in sub:
        list.insert(int(sub[1]), int(sub[2]))
    elif 'print' in sub:
        print(list)
    elif 'remove' in sub:
        list.remove(int(sub[1]))
    elif 'append' in sub:
        list.append(int(sub[1]))
    elif 'sort' in sub:
        list.sort()
    elif 'pop' in sub:
        list.pop()
    else:
        list.reverse()

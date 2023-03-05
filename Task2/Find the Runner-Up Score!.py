if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newList = list(arr)
    newList.sort()
    for i in range(n-1, 0, -1):
        runner = newList[i]
        if runner > newList[i-1]:
            runner = newList[i-1]
            break
    print(runner)

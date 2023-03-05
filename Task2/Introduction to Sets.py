
    
def average(array):
    """
    Function to return distinct average from an array.
    """
    dist_ele = set(array)
    dist_len = len(dist_ele)
    result = sum(dist_ele)/ dist_len
    return ("%.3f" % result)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

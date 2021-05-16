def binary_search(array, start, end):
    while start <= end:
        mid=(start+end) // 2 #index 
        if array[mid] == mid: #중간 array[i]값과 index값이 같으뇨
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1

N = int(input())

array = list(map(int, input().split()))

result = binary_search(array, 0, N-1)
print(result)
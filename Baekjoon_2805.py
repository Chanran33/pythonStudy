def maxSetting(start, end, M, trees):
    while start <= end:
        mid=(start + end) // 2 #나무길이 index값 아님
        sum = 0
        for tree in trees:
            if(tree > mid):
                sum += (tree - mid)
        if sum >= M : 
            result = mid
            start = mid + 1
        elif sum <= M :
            end = mid - 1
    return result
        

N,M = map(int,input().split())
trees = list(map(int,input().split()))
print(maxSetting(0, max(trees), M, trees))

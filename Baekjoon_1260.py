N, M, V = map(int, input().split()) #N은 정점의 개수, M은 간선의 개수, V는 탐색 시작 정점
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [False] * (N+1) #방문 여부 확인

#M(간선)이 연결하는 두 정점 -> 인접리스트 방식 사용
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

#깊이 우선 탐색(DFS)
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, N+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

#너비 우선 탐색(BFS)
def bfs(v):
    queue = [v]
    visited[v] = False
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, N+1):
            if visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = False

dfs(V)
print()
bfs(V)
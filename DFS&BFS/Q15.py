#Q15. 특정 거리의 도시 찾기
#https://www.acmicpc.net/problem/18352
from collections import deque
import sys
input = sys.stdin.readline
n,m,k,x = map(int,input().split())

graph = [[]*(n+1) for _ in range(n+1)]
visited = [-1]*(n+1)

for _ in range(m):
    s,f = map(int,input().split())
    graph[s].append(f)


def bfs(x,k):
    queue = deque()
    queue.append(x)
    visited[x] = 0
    result = []
    while queue:
        nx = queue.popleft()
        for i in graph[nx]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[nx] + 1
                if visited[i] == k:
                    result.append(i)
    if result:
        result.sort()
        for i in result:
            print(i)    
    else:
        print(-1)

bfs(x,k)
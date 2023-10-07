#5-11 미로 탈출
#BFS를 활용해 최단 거리 구하기 

from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#BFS
def bfs(x,y):
    queue = deque()
    #시작노드 큐에 삽입 
    queue.append((x,y))
    #큐가 빌 때까지
    while queue:
        #최상단 노드 빼고
        x,y = queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            #공간을 벗어난 경우 무시
            if nx <0 or ny <0 or nx>=n or ny>=m:
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            #인접하고 처음 방문하면
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 #전꺼에서 플러스 
                queue.append((nx,ny)) #큐에 삽입
    return graph[n-1][m-1]

print(bfs(0,0))
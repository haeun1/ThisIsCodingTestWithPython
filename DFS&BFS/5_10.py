#5-10 음료수 얼려 먹기
#dfs를 활용하여 0으로 연결되어있는 component 갯수 세기 
n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input()))) #숫자로 된 2차원 리스트 입력받기

def dfs(x,y):
    #범위를 벗어나면 즉시 종료
    if x<= -1 or x>=n or y<= -1 or y >= m:
        return False
    #현재 노드를 아직 방문하지 않았다면:
    if graph[x][y] == 0:
        graph[x][y] = 1 #해당 노드 방문 처리
        #상하좌우 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        #상하좌우 다 끝났으면 True 리턴
        return True
    return False #방문했으면 false 반환

#모든 노드에 대해서 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)

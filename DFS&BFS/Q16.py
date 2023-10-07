#Q16. 연구소
#https://www.acmicpc.net/problem/14502
import sys
import copy
input = sys.stdin.readline
from itertools import combinations

n, m = map(int,input().split())
arr = []
place0 = []
place2 = []

for i in range(n):
    data = list(map(int,input().split()))
    for j in range(m):
        if data[j] == 0:
            place0.append((i,j))
        if data[j] == 2:
            place2.append((i,j))
    arr.append(data)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

result = 0 

def dfs(x,y,mat):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #print(nx,ny)
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if mat[nx][ny] == 1 or mat[nx][ny] == 2:
            continue
        if mat[nx][ny] == 0:
            mat[nx][ny] = 2
            dfs(nx,ny,mat)

result = 0
combinationsz = list(combinations(place0,3))
#print(len(place0))
#print(len(combinationsz))
for combination in combinationsz: #3개의 조합마다
    #print(combination)
    mat = copy.deepcopy(arr)
    for i,j in combination:
        mat[i][j] = 1
     
    #dfs 돌려서 인접한 애들 2로 바꾸고 0의 갯수 
    for i,j in place2:
        dfs(i,j,mat)

    count = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0 :
                count += 1
            #print(mat[i][j],end=" ")
        #print()
    result = max(result,count)
    #break

    
print(result)




#Q17. 경쟁적 전염
#https://www.acmicpc.net/problem/18405
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

arr = []
dlist = []
queue = deque()
h = []
for i in range(n):
    data = list(map(int,input().split()))    
    for j in range(n):
        if data[j] != 0:
            dlist.append((data[j],i,j,0))
    arr.append(data)

dlist.sort()
#print(dlist)
for i in dlist:
    queue.append(i)
#queue = deque(dlist)
s , x, y = map(int,input().split())

dx = [-1,1,0,0] 
dy = [0,0,-1,1]

while queue:
    v, a,b,second = queue.popleft()
    if second == s:
        break   
    for i in range(4):
        na = a + dx[i]
        nb = b + dy[i]
        if na<0 or na>=n or nb <0 or nb >= n:
            continue
        if arr[na][nb] == 0 :
            arr[na][nb] = v
            queue.append((v,na,nb,second+1))

print(arr[x-1][y-1])
#4-1 상하좌우 
n = int(input())
data = input().split()
dic = {"L":0,"R":1,"U":2,"D":3}
#L,R,U,D
dx = [0,0,-1,+1]
dy = [-1,+1,0,0]

x = 0
y = 0 
for i in data:
    if (0<=x + dx[dic[i]]<5) and (0<=y + dy[dic[i]]<5): 
        x += dx[dic[i]]
        y += dy[dic[i]]

print(x+1,y+1)
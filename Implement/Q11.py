#Q11 뱀
import sys
input = sys.stdin.readline #입력 시간 줄이기 

n = int(input()) #보드의 크기 
board = [[0]*n for _ in range(n)]#1~n행렬

k = int(input()) #사과의 갯수
for _ in range(k): #사과의 위치
    i,j = map(int,input().split())
    board[i-1][j-1] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

dir = {0:'D'} #방향초,방향
l = int(input()) #방향 전환 수 
for _ in range(l):
    i,j = input().split()
    dir[int(i)] = j

sx , sy = 0,0 #뱀의 머리 
fx , fy = 0,0 #뱀의 꼬리

sec = 0 #시간
bam = 0 #뱀이 바라보고 있는 방향
board[0][0] = 2
q = []

while True:

    if sec in dir.keys(): #방향 바꾸기 
        if dir[sec] == 'D':
            bam += 1
        else:
            bam -= 1

    if bam == -1 :
        bam = 3
    if bam == 4:
        bam = 0 

    #머리를 한 칸 가기   
    sx = sx + dx[bam]
    sy = sy + dy[bam] 
    sec += 1
    #뱀의 경로 저장 꼬리가 뒤따라갈 용 
    q.append((sx,sy))
    #print(q)
    # 자기자긴의 몸과 부딪히거나, 벽을 만나면 끝내기
    if sx < 0 or sx >= n or sy < 0 or sy >= n:
        break
    elif board[sx][sy] == 2:
        break
    #만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    elif board[sx][sy] == 1 :
        board[sx][sy] = 2    
    #만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    else:
        board[sx][sy] = 2
        board[fx][fy] = 0
        fx,fy = q.pop(0) #튜플을 pop해서 하나씩 바로 저장
        #finish = q.pop(0)
        #fx = finish[0]
        #fy = finish[1]
    

print(sec)


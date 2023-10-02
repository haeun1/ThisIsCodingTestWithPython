### 숫자카드게임 

n, m = map(int,input().split()) #n*m 행렬
a = [] # n*m 행렬
minarr = [] #행마다 min값을 저장할 리스트
for _ in range(n): #행마다
    row = list(map(int,input().split())) #행 입력
    a.append(row) 
    minarr.append(min(row)) #행의 최소값을 min리스트에 입력
    #result = max(result,min(row)) => min리스트를 안쓰는 방법
print(max(minarr)) #min리스트의 최대값 출력
    
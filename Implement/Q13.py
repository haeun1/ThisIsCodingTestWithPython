#Q13. 치킨 배달 
#https://www.acmicpc.net/problem/15686
import sys
input = sys.stdin.readline #입력 시간 줄이기 
from itertools import combinations #조합 라이브러리!!

n, m = map(int,input().split())
city = []
for _ in range(n):
    city.append(list(map(int,input().split())))

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

#chicken 중에 조합 m개 고르기 
cbs = list(combinations(chicken,m)) #조합만들어서 리스트에 저장!!

result = []

for cb in cbs: #조합중에 하나 고르기
    h_c_s = []
    for h in home: # 집 중 하나
        h_c = 1000
        for c in cb: #치킨집 m개
            if h_c > abs(c[0]-h[0])+abs(c[1]-h[1]): #절댓값함수 abs()
                h_c = abs(c[0]-h[0])+abs(c[1]-h[1])
        h_c_s.append(h_c)
    result.append(sum(h_c_s))
  
print(min(result))    

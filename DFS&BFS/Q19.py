#Q19. 연산자 끼워 넣기
#https://www.acmicpc.net/problem/14888
import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
data = list(map(int,input().split()))
a,b,c,d = map(int,input().split())
option = ['+']*a + ['-']*b + ['*']*c + ['//']*d 

permutation = list(permutations(option,len(option)))

maxresult = -9999999999
minresult = 9999999999
for per in permutation:
    #print(per)
    result = data[0]
    for i in range(len(per)):
        if per[i] == '+':
            result += data[i+1]
        elif per[i] == '-':
            result -= data[i+1]
        elif per[i] == '*':
            result *= data[i+1]
        else :
            if result < 0:
                result = - ( (-result) // data[i+1]) 
            else:
                result //= data[i+1]
    maxresult = max(maxresult,result)
    minresult = min(minresult,result)

print(maxresult)
print(minresult)


#DFS를 이용해서 푸는 방법

n = int(input().rstrip())
data = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

min_value = 1e9
max_value = -1e9

def dfs(i,now):
    global min_value,max_value,add,sub,mul,div
    #모든 연산자를 다 사용하면, 최소값 최대값 업데이트
    if i == n:
        min_value = min(min_value,now)
        max_value = max(max_value,now)
    else:
        if add>0:
            add -= 1
            dfs(i+1,now+data[i])
            add += 1
        if sub>0:
            sub -=1
            dfs(i+1,now-data[i])
            sub += 1
        if mul>0:
            mul -= 1
            dfs(i+1,now*data[i])
            mul += 1
        if div>0:
            div -= 1
            dfs(i+1,int(now/data[i]))
            div += 1



dfs(1,data[0])
print(max_value)
print(min_value)

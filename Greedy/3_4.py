### 1이 될 때까지

n, k = map(int,input().split())

count = 0 #횟수 
while n != 1: #n이 1이 될 때까지
    if n%k==0: #k로 나눌 수 있으면
        n = n//k #나누고
    else: #나눌 수 없으면
        n -= 1 #1을 빼자
    count += 1 #횟수 카운트 

print(count) #횟수 출력

#책에서 나온 다른 효율적 방법:
# n이 k로 나누어 떨어지는 수가 되게만들고 그만큼 result를 플러스
# n을 k로 나눔
# 이를 반복 
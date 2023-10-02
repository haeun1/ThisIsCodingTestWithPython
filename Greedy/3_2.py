### 큰 수의 법칙

n,m,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True) # 가장 큰수랑 두번째로 큰 수를 구하기 위해 정렬
result = 0 
count = 0 
for i in range(m):
    if count == k: #k번 더했으면 초기화
        count = 0 
        result += a[1] # 두번째 수 더하기
    else:
        count += 1 
        result += a[0] # k번까진 첫번째 수 더하기 

print(result)

#반복되는 수열을 이용하는 방법
arr = [a[0]]*k + [a[1]] #반복되는 수열을 만들기 
i = m//(k+1) # 완전하게 반복되는 수열이 총 몇번? 
result = 0
result = sum(arr)*i #완전하게 반복되는 수열의 합에 횟수를 곱하기 
j = m%(k+1) #마지막 불완전한 수열의 인덱스
for k in range(j):
    result += arr[k] #인덱스까지만 더하기 
print(result)

# 책에서 나온 방법: 
# 가장 큰 수가 더해지는 횟수: count = int(m/(k+1))*k + m%(k+1)
# 두번째로 큰 수가 더해지는 횟수: m - count 
# 결과: count * a[0] + (m-count) * a[1]
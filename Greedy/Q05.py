#Q05. 볼링공 고르기 
n, m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
result = 0

for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        if data[i] == data[j]:
            continue
        else: 
            result += n - j 
            break

print(result)

#효과적으로 푸는 방법
arr = [0] * 11 #무게를 담는 리스트
for x in data:
    arr[x] += 1 #무게마다 +1 

result = 0
for i in range(1,m+1): #무게에 따라
    n -= arr[i] #A 제외
    result += arr[i] * n 

print(result)



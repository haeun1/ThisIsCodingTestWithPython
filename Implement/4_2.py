#4-2 시각
#내가 푼 방법
# 수학적 경우의 수로 계산
n = int(input())
result = 0
for i in range(n+1):
    if i%10 == 3 :
        result += 3600
    else:
        result += 3600 - 5*9*5*9 
print(result)


#책의 방법
#000000~235959까지 일일이 세기 문자열에 3이 포함되어있으면 카운트 증가
h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1
print(count)

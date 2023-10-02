### 모험가 길드
n = int(input())
a = list(map(int,input().split()))
a.sort()
group = 0
i = 0

while i<n and i + a[i] - 1 < n :
    j = a[i]
    k = 0
    flag = True
    for k in range(1,j):
        if a[i]<a[i+k]:
            flag = False
            break
    if flag : 
        group += 1
        i += j 
    else:
        i += 1

print(group)


#책의 방법
# for i in data: #공포도를 낮은 것부터 하나씩 확인하면서
#   count+=1 : 그룹의 회원수 +1 
#   if count >= i #현재 공포도보다 지금의 회원수가 그 이상이면 그룹 결성
#       result+=1 : 그룹 수 +1
#       count = 0 : 그룹의 회원수 초기화 


    
        
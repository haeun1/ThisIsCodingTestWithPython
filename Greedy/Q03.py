#Q03. 문자열 뒤집기
#백준 1439번 

s = input()
arr = []
for i in s:
    arr.append(int(i)) #숫자문자열을 리스트로 

group1 = 1 #첫번째 원소의 group
group2 = 0 #첫번째원소와 다른 숫자의 group
flag = True #숫자가 바뀌는 flag
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]: #다음숫자가 달라지면 
        flag = not flag #flag를 뒤집고
        if flag: #다른 그룹의 수를 +1
            group1 += 1
        else:
            group2 += 1

print(min(group1,group2)) #group개수가 작은 게 정답 

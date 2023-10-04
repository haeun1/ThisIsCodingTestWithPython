#Q08 문자열 재정렬
s = input()
result = []
sum = 0 

for i in s:
    if ord('A') <= ord(i) <= ord('Z'):
        result.append(i)
    else:
        sum += int(i) 

result.sort()
if sum !=0:
    result += str(sum)

#리스트를 문자열로 변환: join 함수!!!
print(''.join(result))
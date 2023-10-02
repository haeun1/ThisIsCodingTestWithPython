### Q2. 곱하기 혹은 더하기
s = input()
arr = []
for i in s:
    arr.append(int(i))

result = arr[0]

#비교하는 두 수 중에서 하나라도 0이거나, 1이면 더하고, 2이상이면 곱하는 게 좋음
for i in range(1,len(arr)):
    if result < 2 or arr[i] < 2:
        result += arr[i]
    else:
        result *= arr[i]
print(result) 
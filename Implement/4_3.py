#4_3 왕실의 나이트 
state = input()

row = int(state[1])-1
col = ord(state[0])-ord('a')

arr = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

count = 0

for d in arr:
    if (0 <= (row + d[0]) < 8) and (0 <= (col + d[1]) < 8):
        count += 1

print(count)
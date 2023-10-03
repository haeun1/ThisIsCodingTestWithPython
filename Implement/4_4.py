#4_4 게임 개발
n, m = map(int,input().split())
i, j, d = map(int,input().split())
gmap = []
for _ in range(n):
    gmap.append(list(map(int,input().split())))

dic = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}
gmap[i][j] = 2
count = 0
result = 1
while True:
    newx = i + dic[d][0]
    newy = j + dic[d][1]
    
    if count == 4:
        #뒤로 갈 수 있을 때 뒤로 감 
        newx = i - dic[d][0]
        newy = j - dic[d][1]
        if gmap[newx][newy] == 1:
            break
        else:
            i = newx
            j = newy
            count = 0

    if gmap[newx][newy] == 0:
        count = 0
        i = newx
        j = newy
        d = (d+1)%4
        gmap[i][j]=2
        result += 1
        continue
    else: 
        count += 1 
        d = (d+1)%4
        
print(result)
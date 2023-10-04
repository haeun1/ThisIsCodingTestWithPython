#Q10. 자물쇠와 열쇠 
#https://school.programmers.co.kr/learn/courses/30/lessons/60059

#2차원 리스트 90도 회전 외워두자!!
def rotate(m,key):
    arr = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            arr[j][m-i-1] = key[i][j]
    return arr

def solution(key, lock):
    answer = False
    
    m = len(key)
    n = len(lock)
    a = 0
    for l in lock:
        a += l.count(0) #2차원의 0의 갯수를 세는 법 한 행마다 세서 더하기!!!!!!
    
    for _ in range(4):
        if answer == True:
            break
        key = rotate(m,key)
        for p in range(-m+1,n):
            if answer == True:
                break
            for q in range(-m+1,n):
                count = 0
                for i in range(m):
                    for j in range(m):
                        if 0 <= p+i < n and 0 <= q+j < n:
                            if key[i][j] == 1 and lock[p+i][q+j] == 1:
                                count = 0 
                                break
                            elif key[i][j] == 0 and lock[p+i][q+j] == 0:
                                count = 0
                                break
                            elif key[i][j] == 1 and lock[p+i][q+j] == 0:
                                count += 1
                if count == a:
                    answer = True
                    break
                    
    
    return answer
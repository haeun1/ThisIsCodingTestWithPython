#Q09. 문자열 압축
#https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    result = 1001
    
    for i in range(1,len(s)+1):
        temp = []
        count = 1
        for j in range(0,len(s),i): # 0~7
            if s[j:j+i] == s[j+i:j+2*i]:
                count += 1
            else:
                if count!=1:
                    temp += str(count)+s[j:j+i]
                else:
                    temp += s[j:j+i]
                count = 1
        if len(temp) < result :
            result = len(temp)
    return result
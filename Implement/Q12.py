#Q12. 기둥과 보 설치
#https://school.programmers.co.kr/learn/courses/30/lessons/60061

#1회차 . 코드길이가 매우 길고 모든 상황에 따라 조건문을 나누었음. 정답은 맞았으나 코드짜는 시간이 너무 오래걸림 3시간 걸림  
def delete(x,y,a,pwall,qwall):
    result = False
    if a == 0: #기둥
        #위에 아무것도 없거나
        if pwall[x][y+1] == 0 and qwall[x][y+1] == 0 and qwall[x-1][y+1] == 0:
            result = True
        #위에 기둥이 있는 경우 
        if pwall[x][y+1] == 1:        
            if qwall[x][y+1] == 1 or qwall[x-1][y+1] == 1: #보의 한쪽 끝 부분 
                result = True
            else:
                return False            
        #위에 보가 있는데 그 보가 설치가 가능하면 
        if qwall[x][y+1] == 1:   
            #한쪽 끝 부분이 기둥 위에 있거나 
            if pwall[x+1][y] == 1:
                result = True
            #양쪽 끝부분이 다른보와 인접
            elif qwall[x-1][y+1] == 1 and qwall[x+1][y+1] == 1: 
                result = True
            else:
                return False
        if qwall[x-1][y+1] == 1:
            #한쪽 끝 부분이 기둥 위에 있거나 
            if pwall[x-1][y] == 1:
                result = True
            #양쪽 끝부분이 다른보와 인접
            elif qwall[x-2][y+1] == 1 and qwall[x][y+1] == 1: 
                result = True
            else:
                return False
    else: #보
        #위에 아무것도 없는 경우 
        if pwall[x][y] == 0 and pwall[x+1][y] == 0 and qwall[x+1][y] == 0 and qwall[x-1][y] == 0:
            result = True
            
        #위에 기둥이 있는 경우 
        if pwall[x][y] == 1:  
            if qwall[x-1][y] == 1: #보의 한쪽 끝 부분 
                result = True
            elif pwall[x][y-1] == 1: #다른 기둥 위
                result = True
            else:
                return False
        if pwall[x+1][y] == 1: 
            if qwall[x+1][y] == 1 : #보의 한쪽 끝 부분 
                result = True   
            elif pwall[x+1][y-1] == 1: #다른 기둥 위
                result = True
            else:
                return False
        #인접하는 보가 있는 경우 
        if qwall[x+1][y] == 1:
            #한쪽 끝 부분이 기둥 위에 있거나 
            if pwall[x+1][y-1] == 1 or pwall[x+2][y-1] == 1:
                result = True
            else:
                return False
        if qwall[x-1][y] == 1:
            #한쪽 끝 부분이 기둥 위에 있거나 
            if pwall[x-1][y-1] == 1 or pwall[x][y-1] == 1:
                result = True
            else:
                return False
    return result

def solution(n, build_frame):
    answer = []
    
    pwall = [[0]*(n+1) for _ in range(n+1)] #기둥
    qwall = [[0]*(n+1) for _ in range(n+1)] #보
 
    for build in build_frame:
        x,y, a, b = build
        if a == 0: #기둥
            if b == 0: #삭제
                #삭제가능한 지 알아보기
                if delete(x,y,a,pwall,qwall):
                    pwall[x][y] = 0
                    
            else: #설치
                if pwall[x][y] == 0 and y == 0: #바닥에 설치
                    pwall[x][y] = 1
                    
                elif qwall[x][y] == 1 or qwall[x-1][y] == 1: #보의 한쪽 끝 부분 
                    pwall[x][y] = 1
                    
                elif pwall[x][y-1] == 1: #다른 기둥 위
                    pwall[x][y] = 1
                    
        else: #보 
            if b == 0: #삭제
                #삭제가능한지 알아보기 
                if delete(x,y,a,pwall,qwall):
                    qwall[x][y] = 0
                    
            else: #설치
                #한쪽 끝 부분이 기둥 위에 있거나 
                if pwall[x][y-1] == 1 or pwall[x+1][y-1] == 1:
                    qwall[x][y] = 1
                    
                #양쪽 끝부분이 다른보와 인접
                elif qwall[x-1][y] == 1 and qwall[x+1][y] == 1: 
                    qwall[x][y] = 1
                    
    
    for i in range(n+1):
        for j in range(n+1):
            if pwall[i][j] == 1:
                answer.append([i,j,0])
            if qwall[i][j] == 1:
                answer.append([i,j,1])
    
    return answer


#2회차 모든 경우를 조건으로 나누지 말고 그냥 되는 지 안되는 지 체크하는 방향으로 책의 방법으로 해보자
def possible(answer):
    for x,y,a in answer: #answer에서 리스트 꺼내서 원소들을 저장
        if a == 0 : #기둥인 경우
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer: # 설치할 수 있는 경우 
                continue
            return False #아니면 false 반환
        elif a == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue #설치할 수 있는 경우
            return False #아니면 false 반환
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,a,b = frame
        if b == 0: #삭제
            answer.remove([x,y,a]) #일단 지우고
            if not possible(answer): #가능한 지 확인
                answer.append([x,y,a]) #불가능하면 다시 추가
        if b == 1: #설치
            answer.append([x,y,a]) #일단 설치하고
            if not possible(answer): #가능한 지 확인
                answer.remove([x,y,a]) #불가능 하면 삭제 
                
    return sorted(answer) #리스트를 정렬하여 반환
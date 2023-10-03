#Q06. 무지의 먹방 라이브
# https://school.programmers.co.kr/learn/courses/30/lessons/42891

#1회 풀었을 때 , 정확성은 맞으나 효율성이 떨어짐 
def solution(food_times, k):
    answer = 0
    n = 0
    i = 0
    flag = False
    if k >= sum(food_times):
        answer = -1 
    else:
        while True:
            if i == len(food_times):
                i = 0

            if food_times[i] == 0:
                i += 1
                continue
            else:
                if flag:
                    answer = i%len(food_times) + 1
                    break
                food_times[i] -= 1
                k -= 1 
                i += 1
                if k == 0 :
                    flag = True
                 
    return answer 


##정답
import heapq #우선순위 큐 

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    #시간이 작은 음식부터 빼야 하므로 우선순위 큐 이용
    q = [] 
    for i in range(len(food_times)):
        # (음식시간, 음식번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q,(food_times[i],i+1))
    
    sum_value = 0 #먹기 위해 사용한 시간
    previous = 0 #직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수
    
    #그동안 사용한 시간 + (앞으로 음식 시간)*현재음식 개수 와 k 비교
    while sum_value + ((q[0][0]-previous)*length) <= k:
        now = heapq.heappop(q)[0] #첫번째 음식 뺌
        sum_value += (now-previous) * length #첫번째음식걸리는 시간 * 음식 갯수 
        length -= 1 #하나 뺏으니 하나 빼기
        previous = now #이전음식시간 업데이트
    
    # 남은 음식 중에서 몇 번째 음식인지 확인
    result = sorted(q,key = lambda x:x[1]) #음식의 번호 기준으로 정렬
    return result[(k-sum_value)%length][1]
        
    
    
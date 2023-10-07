#5-2.py 큐 예제
from collections import deque

#큐 구현을 위해 deque라이브러리 사용 
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #deque([3,7,1,4])
queue.reverse() #reverse함수가 있음!!
print(queue) #4,1,7,3

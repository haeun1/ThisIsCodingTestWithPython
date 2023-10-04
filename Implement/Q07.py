#Q07 럭키 스트레이트 
#https://www.acmicpc.net/problem/18406
n = input()
a = len(n)//2
n1 = 0
n2 = 0
for i in range(a):
    n1 += int(n[i])
    n2 += int(n[i+a])
if n1 == n2:
    print("LUCKY")
else:
    print("READY")
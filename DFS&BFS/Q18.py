#Q18. 괄호 변환
#https://school.programmers.co.kr/learn/courses/30/lessons/60058
#책의 풀이가 더 좋은 것 같음 
#str은 원소 변경이 불가능하다 따라서 list로 바꿔서 변경 후 다시 join함수 써서 str로 변환. 
import copy
def dfs(w):
    if w == "":
        return w
    
    temp2 = copy.deepcopy(w)
    for i in range(len(w)//2):
        temp2 = temp2.replace('()',"")
    if temp2 == "":
        return w
        
    for i in range(2,len(w)+1,2):
        u = w[0:i]
        v = w[i:len(w)]
        if u.count('(') == u.count(')'):
            temp = copy.deepcopy(u)
            for _ in range(i//2):
                temp = temp.replace('()','')
            if temp != "": # 빈문자열이 아니라면
                s = '('
                s += dfs(v)
                s += ')'
                s += "".join([ ')' if i == '(' else '(' for i in u[1:-1] ])
                return s
            else: #빈문자열이라면
                return u + dfs(v)
                pass

def solution(p):
    return dfs(p)


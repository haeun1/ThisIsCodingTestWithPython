#5-3 재귀 함수 예제

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

#무한히 출력되다가 재귀 최대 깊이를 초과했다는 내용이 나오고 recursionerror
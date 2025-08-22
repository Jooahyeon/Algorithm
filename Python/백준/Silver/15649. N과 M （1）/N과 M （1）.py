import sys
sys.setrecursionlimit(10 ** 6) # 재귀 한도 늘리기(런타임에러 방지)

input = sys.stdin.readline

def backtracking():
    # 종료 조건 : array에 담긴 숫자 개수가 목표 m에 도달하면 출력
    if len(array) == m:
        print(" ".join(map(str, array)))
        return
    
    # 1부터 n까지 후보를 순서대로 시도
    for i in range(1, n + 1):
        # 중복방지 - 이미 선택된 숫자 건너뜀
        if i not in array:
            array.append(i)           # 선택(상태 변경)
            backtracking()            # 다음 깊이로 진행
            array.pop()               # 되돌리기 : 방금 넣은 원소 다시 제거
            
n, m = map(int,input().split())       # "n, m" 형태의 한 줄을 받아 정수로 변환
array = []                            # 선택한 수열을 스택 역할의 리스트 
backtracking()                        # 탐색 시작
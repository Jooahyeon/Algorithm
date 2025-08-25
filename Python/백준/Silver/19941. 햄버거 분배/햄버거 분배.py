# 사람 위치 리스트 P[], 햄버거 위치 리스트 H[]를 만든 뒤 투 포인터로 매칭 방식 -> O(N)

import sys
input = sys.stdin.readline                 # 함수 바인딩

N,K = map(int, input().split())            # 입력: N = 자리 수, K = 허용 거리
S = input().rstrip()                       # 오른쪽 개행 제거

# H와 P의 인덱스를 각각 따로 리스트에 저장
H = [i for i, c in enumerate(S) if c == 'H']
P = [i for i, c in enumerate(S) if c == 'P']

# 두 포인터 : i(햄버거), j(사람)
i = j = ans = 0

# 각 포인터가 햄버거나 사람을 다 처리할 때까지 반복함
while i < len(H) and j < len(P):
    
    # 현재 햄버거와 사람의 거리가 K 이하이면 매칭
    if abs(H[i] - P[j]) <= K:
        ans += 1
        i += 1
        j += 1
        
    # 햄버거가 사람보다 왼쪽에 있어 안닿는 경우 버려
    elif H[i] < P[j] - K:
        i += 1
    # 반대상황 : 사람이 햄버거보다 너무 왼쪽이라 닿을 수 없는 경우 버려 (다음사람 이동)
    else:                                 #P[j] < H[i] - K
        j += 1
        
print(ans)

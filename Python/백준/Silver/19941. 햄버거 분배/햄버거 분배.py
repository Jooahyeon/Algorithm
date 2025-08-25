import sys
input = sys.stdin.readline

N, K = map(int,input().split())
S = input().rstrip()                   #rstrip() 인자 없을 경우 오른쪽 공백 제거
eat_list = list(S)
cnt = 0

for i in range(len(eat_list)):
    if eat_list[i] == "P":
        for j in range(i-K, i+K+1):
            if 0 <= j < N and eat_list[j] == "H":
                cnt += 1
                eat_list[j] = "0"
                break
print(cnt)
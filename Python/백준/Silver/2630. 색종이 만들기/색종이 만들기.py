# 첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.
# 분할 정복 / 재귀

# 색칠한 부분의 색이 나머지 부분의 색과 같으면 +1
# 색이 다르면 분할 정복(색이 같을 때까지 나눠)
# 색 확인하는 것은 이중 for문 활용


import sys         # 입출력

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
white = 0
blue = 0

def cut(x, y, n):
    global white, blue
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:                   # 색이 다른 경우
                cut(x , y, n // 2)                     # 1
                cut(x , y + n // 2, n // 2 )           # 2
                cut(x + n // 2, y, n // 2)             # 3
                cut(x + n // 2, y + n // 2, n // 2)    # 4
                return
    if color == 0:
        white += 1
    else:
        blue += 1

cut(0, 0, N)
print(white)
print(blue)
                

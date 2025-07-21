# 남는 사탕은 없어야 한다.
# 남규는 영훈이보다 2개 이상 많은 사탕을 가져야 한다.
# 셋 중 사탕을 0개 받는 사람은 없어야 한다.
# 택희가 받는 사탕의 수는 홀수개가 되어서는 안 된다.

candy = int(input())

answer = 0
for A in range(0, candy+1): # 0개 ~ 6개
    for B in range(0,candy+1):
        for C in range(0,candy+1):
            if A + B + C == candy:
                if A >= B+2 :
                    if A !=0 and B != 0 and C != 0:
                        if C % 2 == 0:
                            answer += 1
print(answer)
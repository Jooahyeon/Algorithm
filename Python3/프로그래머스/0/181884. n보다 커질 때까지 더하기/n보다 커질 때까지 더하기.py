def solution(numbers, n):
    answer = 0

#     1. 배열 입력 받기
#     2. 입력받은 배열 합 (조건 sum < n)
#     

    for i in numbers :
        answer += i
        if answer > n :
            return answer 

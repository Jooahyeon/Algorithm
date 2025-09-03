def solution(sizes):
#     1. w(가로)의 최대 값 Max_w, h(세로)의 최대 값 Max_h 구하기
#     2. Max_h > Max_w인 경우(or 반대인 경우), 현재 Max_w를 제외한 최대값 다시 구하기
#     3. 최종으로 나온 최대값 곱하여 크기 return 

    w = [] 
    h = []
    
    for i in sizes:
        w.append(max(i))
        h.append(min(i))
        
    return max(w) * max(h)
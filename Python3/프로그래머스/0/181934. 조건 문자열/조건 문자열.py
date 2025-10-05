def solution(ineq, eq, n, m):
    
    answer = str(n) + ineq + eq.replace('!', '') + str(m)
    
    return int(eval(answer))
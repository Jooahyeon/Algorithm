TC = int(input())

for _ in range(TC):
    number = int(input()) 
    
    for i in range(2, 1_000_001):
        if number % i == 0: # 100만 이하의 약수가 존재함!
            print("NO")
            break
        if i == 1_000_000:  # 100만 이하의 약수가 존재하지 않음!
            print("YES")
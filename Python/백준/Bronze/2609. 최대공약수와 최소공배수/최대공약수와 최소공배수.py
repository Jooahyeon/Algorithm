def gcd(x,y):
    while(y):
        x, y = y ,x % y
    return x
    
num1,num2=map(int,input().split())
result=gcd(num1,num2)
print(result)
print(int(num1*num2/result))
# 11653: 소인수분해

num = int(input())
result = []
while num > 1:
    for n in range(2, num+1):        
        if num % n == 0:
            result.append(n)
            num //= n
            break
            
for r in result:
    print(r)


"""
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
"""
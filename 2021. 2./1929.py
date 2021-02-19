# 1929: 소수 구하기

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)

"""
# 시간초과
for i in range(M, N):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        print(i)
"""

"""
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
"""
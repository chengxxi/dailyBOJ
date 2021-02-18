# 1978: 소수 찾기

N = int(input())
nums = list(map(int, input().split()))
prime = 0
for n in nums:
    cnt = 0
    for i in range(1, n+1):
        if n%i==0:
            cnt += 1
    if cnt == 2:
        prime += 1
print(prime)


"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""
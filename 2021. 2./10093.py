# 10093: 숫자

a, b = map(int, input().split())

if a != b:
    if a > b:
        a, b = b, a
    print(b-a-1)
    print(*range(a+1, b))
else:
    print(0)


"""
두 양의 정수가 주어졌을 때, 두 수 사이에 있는 정수를 모두 출력하는 프로그램을 작성하시오.
"""
# 1193: 분수찾기

x = int(input())
line = 1

while x > line:
    x -= line
    line += 1

if line % 2 == 0: # x 아니고 line
    t = x
    b = line - x + 1
else:
    t = line - x + 1
    b = x

print("{}/{}".format(t,b))


# def fraction(num):
#     line = 1
#     # 대각선으로 몇 번째 줄에 위치하는지 찾기
#     while num > line:
#         num -= line
#         line += 1
#
#     if line % 2 == 1: # 여기도 num 아니라 line! 그래서 안된듯
#         t = num
#         b = line-num+1
#     else:
#         t = line-num+1
#         b = num
#
#     return t, b
#
# x = int(input())
# t, b = fraction(x)
#
# print("{}/{}".format(t,b))


"""
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로
차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
"""
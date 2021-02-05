# 14491: 9진수

T = int(input())
base = 9
answer = []

while True:
    res = divmod(T, base)
    q = res[0]; r = res[1]
    answer.append(str(r))
    if q == 0:
        break
    else:
        T = q

answer.reverse()
print("".join(answer))

"""
10진수를 9진수로 바꾸자.
"""
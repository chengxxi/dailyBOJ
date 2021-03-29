# 12871: 무한 문자열

# 최소공배수 구하기
def gcd(n1, n2):
    while n1%n2 != 0:
        (n1, n2) = (n2, n1%n2)
    return n2


s = input()
t = input()

if len(s) == len(t):
    if s == t: print(1)
    else: print(0)
else:
    g = gcd(len(s), len(t))
    lcm = len(s) * len(t) / g
    ss = int(lcm / len(s))
    tt = int(lcm / len(t))

    if s * ss == t * tt:
        print(1)
    else: print(0)






"""
문자열 s가 있을 때, f(s)는 s를 무한번 붙인 문자열로 정의한다.
예를 들어, s = "abc" 인 경우에 f(s) = "abcabcabcabc..."가 된다.

다른 문자열 s와 t가 있을 때, f(s)와 f(t)가 같은 문자열인 경우가 있다.
예를 들어서, s = "abc", t = "abcabc"인 경우에 f(s)와 f(t)는 같은 문자열을 만든다.

s와 t가 주어졌을 때, f(s)와 f(t)가 같은 문자열을 만드는지 아닌지 구하는 프로그램을 작성하시오.
"""
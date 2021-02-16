# 11944: NN

import sys
n, m = map(int, sys.stdin.readline().split())
num = str(n) * n
print(num[:m])

"""
문제는 매우 간단하다. N을 N번 출력하는 프로그램을 작성하여라. 다만, 답이 길어지는 경우 답의 앞 M자리만 출력한다.
"""
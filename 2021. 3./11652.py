# 11652: 카드

from collections import Counter

num = int(input())
nlist = [int(input()) for _ in range(num)]
ndict = Counter(sorted(nlist))
maxval = 0
for i in ndict:
    if ndict[i] > maxval:
        maxval = ndict[i]
        index = i
print(index)

"""
준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.

준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오.
만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.
"""
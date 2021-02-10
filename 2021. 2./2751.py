# 2751: 수 정렬하기 2

nlist = []
for n in range(int(input())):
    nlist.append(int(input()))
print("\n".join(map(str, sorted(nlist))))

"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

# 백준에서 시간초과나서 다시 풂
"""
n=int(input())
num=[]

for _ in range(n):
    x = int(input())
    num.append(x)

for i in sorted(num):
    print(i)
"""
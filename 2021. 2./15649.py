# 15649: N과 M (1)

n, m = map(int, input().split())
s = []

def f():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if i in s:
            continue
        s.append(i)
        f()
        s.pop()

f()

# DFS Backtracking


"""
N, M = map(int, input().split())
arr = [a for a in range(1, N+1)]

while M > 0:
    sub = []
    for i in range(1<<N):
        mini = []
        for j in range(N):
            if i & (1<<j):
                mini.append(arr[j])
        sub.append(mini)

    for s in sub:
        if len(s) == M:
            print(*s)
"""


# sub = []
# for i in range(1<<N):
#     mini = []
#     for j in range(N):
#         if i & (1<<j):
#             mini.append(arr[j])
#     sub.append(mini)

# for s in sub:
#     if len(s) == M:
        # print(*s)


"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""
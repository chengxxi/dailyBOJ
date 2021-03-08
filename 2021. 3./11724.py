# 11724: 연결요소의 개수

import sys
n, m = map(int, sys.stdin.readline().split())
edge = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
adj = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(m):
    n1, n2 = edge[i][0], edge[i][1]
    adj[n1][n2] = 1;
    adj[n2][n1] = 1
visited = [0] * (n + 1)

def bfs(i):
    q = []
    q.append(i)
    visited[i] = 1

    while q:
        cur = q.pop(0)
        for j in range(1, n + 1):
            if adj[cur][j] == 1 and visited[j] == 0:
                q.append(j)
                visited[j] = 1
cnt = 0
for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)


"""
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
"""
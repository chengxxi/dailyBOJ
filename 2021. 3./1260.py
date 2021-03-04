# 1260: DFS와 BFS

def dfs(i):
    print(i, end=" ")
    visited[i] = 1

    for j in range(1, n + 1):
        if adj[i][j] == 1 and visited[j] == 0:
            dfs(j)


def bfs(i):
    visited = [0] * (n + 1)
    q = []
    q.append(i)
    visited[i] = 1

    while q:
        cur = q.pop(0)
        print(cur, end=" ")

        for j in range(1, n + 1):
            if adj[cur][j] == 1 and visited[j] == 0:
                q.append(j)
                visited[j] = 1


n, m, v = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]
adj = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    n1, n2 = edge[i][0], edge[i][1]
    adj[n1][n2] = 1;
    adj[n2][n1] = 1

dfs(v)
print()
bfs(v)


"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
"""


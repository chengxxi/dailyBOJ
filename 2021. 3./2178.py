# 2178: 미로 탐색

def is_safe(y, x):
    return 0 <= y < N and 0 <= x < M and maze[y][x] == 1


def bfs(r, c):
    global result
    q.append((r, c))
    visited.append((r, c))

    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if is_safe(nr, nc) and (nr, nc) not in visited:
                q.append((nr, nc))
                visited.append((nr, nc))
                distance[nr][nc] = distance[r][c] + 1

                if nr == N-1 and nc == M-1:
                    result = distance[nr][nc] - 1
                    return


N, M = map(int, input().split())  # N X M
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

result = 0
q = []
distance = [[0] * M for _ in range(N)]

bfs(0, 0)

print(result + 2) # + start & end



"""
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
"""
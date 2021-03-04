# 2606: 바이러스
def dfs(i):
    global result
    result.append(i)
    visited[i] = 1

    for j in range(1, comp+1):
        if adj[i][j] == 1 and visited[j] == 0:
            dfs(j)

comp = int(input())
m = int(input())
edge = [list(map(int, input().split())) for _ in range(m)]
adj = [[0 for _ in range(comp+1)] for _ in range(comp+1)]
visited = [0] * (comp + 1)

for i in range(m):
    n1, n2 = edge[i][0], edge[i][1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

result = []
dfs(1)
print(len(result)-1)


"""
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.


어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
"""
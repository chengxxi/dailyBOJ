# 15650: N과 M (2)

N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
visited = [0] * N
stack = []

### DFS 활용하기
def dfs(cnt):
    if cnt == M:
        print(*stack)
        return
    for i in range(N):
        if visited[i]: continue

        visited[i] = 1
        stack.append(nums[i])
        dfs(cnt+1)
        stack.pop()

        # 순열과의 차이점, 큰 나무에서 전에 봤던 것 닫아주기
        for j in range(i+1, N):
            visited[j]= 0


dfs(0)

### 순열로 시도했다가 실패

# def perm(k): # k: 선택한 원소가 들어갈 자리 (sel에 원소를 넣은 횟수) / 몇 번째 자리에 넣을 것인가?
#     if k == M: # 원소 선택이 끝나면,
#         print(*sel) # 출력하고
#         return # 끝냄
#
#     for i in range(M): # 가지고 있는 원소를 다 살펴본다
#         if visited[i] == 0: # 아직 선택한 게 아니면
#             sel[k] = arr[i] # sel의 k번째에 arr[i]가 위치하도록 한다
#             visited[i] = 1 # 선택되었다고 표시
#             perm(k+1) # 다음 숫자
#             visited[i] = 0 # 다음을 위해 방문배열 초기화
#             # visited 없으면 중복순열
#
#
# N, M = map(int, input().split())
#
# arr = [n for n in range(1, N+1)] # 순열을 만들기 위한 원소
# sel = [0] * M # 만들어진 순열 저장
# visited = [0] * M # 선택여부 저장하기 위한 배열
# # visited 없으면 중복순열 생성됨
#
# perm(0)




"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
"""
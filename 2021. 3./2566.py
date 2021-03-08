# 2566: 최댓값

arr = [list(map(int, input().split())) for _ in range(9)] # 9 X 9
max_val = 0; x = 0; y = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            x = i+1; y = j+1
print(max_val)
print(x, y)


"""
<그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수가 주어질 때, 
이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.
"""
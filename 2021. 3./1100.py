# 1100: 하얀 칸

board = [[0 for _ in range(8)] for _ in range(8)]
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            board[i][j] = 1 # 1: white / 0: black

cnt = 0

status = [list(input()) for _ in range(8)]


for i in range(8):
    for j in range(8):
        if status[i][j] == 'F' and board[i][j] == 1:
            cnt += 1

print(cnt)


"""
체스판은 8*8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 
가장 왼쪽 위칸 (0,0)은 하얀색이다. 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.
"""
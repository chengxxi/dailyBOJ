# 11650: 좌표 정렬하기

nli = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    nli.append((x, y))

nli.sort(key=lambda n: (n[0], n[1]))

for li in nli:
    print(*li)

"""
2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
"""
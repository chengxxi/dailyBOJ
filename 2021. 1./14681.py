# 14681: 사분면 고르기

# A, B = map(int, input().split())
A = int(input())
B = int(input())

if A > 0 and B > 0:
    result = 1
elif A > 0 and B < 0:
    result = 4
elif A < 0 and B < 0:
    result = 3
elif A < 0 and B > 0:
    result = 2
   
print(result)

"""
점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 
단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
"""
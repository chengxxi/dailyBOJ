# 1065: 한수

N = int(input())
hansu = 0
for num in range(1, N+1):
    if num < 100:
        hansu += 1
    else:
        nums = list(map(int, str(num)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            hansu += 1

"""
def count_hansu(number):
    hansu = 0
    for num in range(1, number+1):
        if num < 100:
            hansu += 1
        elif num < 1000:
        # 리스트 작업 안 했음: TypeError
            if num[0] - num[1] == num[1] - num[2]:
                hansu += 1
    return hansu 
"""


print(hansu)

"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
"""
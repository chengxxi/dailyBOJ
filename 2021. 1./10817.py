# 10817: 세 수

nums = list(input().split())
for i in range(len(nums)):
    nums[i] = int(nums[i])
revnums = sorted(nums, reverse=True)
print(revnums[1])

"""
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오
"""
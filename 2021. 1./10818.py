# 10818: 최소, 최대

N = int(input())
nums = list(map(int, input().split()))

maxx = max(nums)
minn = min(nums)

print(minn, maxx)


"""
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
"""
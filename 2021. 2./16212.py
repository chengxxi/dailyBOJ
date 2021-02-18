# 16212: 정열적인 정렬

N = int(input())
# print(' '.join(list(map(str, sorted(list(map(int, input().split())))))))
nums = list(map(int, input().split()))
nums.sort()
print(*nums)


"""
형준이는 수열을 하나 가지고 있다. 형준이는 수열을 정열적으로 정렬해보려 한다. 과연, 정렬할 수 있을까?
"""
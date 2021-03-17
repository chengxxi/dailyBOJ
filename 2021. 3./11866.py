# 11866: 요세푸스 문제 0


n, k = map(int, input().split())
nums = [i for i in range(1, n + 1)]
ans = []
temp = k-1

### 1.
for i in range(n):
    if len(nums) > temp:
        ans.append(nums.pop(temp))
        temp += k-1
    elif len(nums) <= temp:
        temp %= len(nums)
        ans.append(nums.pop(temp))
        temp += k-1


print("<", end='')
for i in ans:
    if i == ans[-1]:
        print(i, end = '')
    else:
        print("{}, ".format(i), end='')
print(">")


### 2.
# print("<",end='')
# i = 0
#
# while len(nums) > 1:
#     i = i + k
#     if i > len(nums):
#         i = i % len(nums)
#         if i == 0 :
#             i = i + len(nums)
#     i = i - 1
#     print(str(nums.pop(i)), end=", ")
#
# print("{}>".format(str(nums.pop())))





# while nums:
#     if k <= len(nums):
#         cur = nums.pop(k)
#         ans.append(cur)
#     else:
#         cur = nums

# i = 0
# while len(ans) <= n:
#     if i + k <= n:
#         ans.append(nums[i+k])
#     else:
#         ans.append(nums[i+k-n])
#     i += k
#

#
# print(*ans)

"""
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
"""
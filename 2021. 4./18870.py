# 18870: 좌표 압축

# ### first trial: quicksort
# def swap(arr, a, b):
#     arr[a], arr[b] = arr[b], arr[a]
#
# def partition(arr, l, r):
#     p = arr[l] # pivot value
#     i = l; j = r
#     while i <= j:
#         if arr[i] <= p:
#             i += 1
#         if arr[j] >= p:
#             j -= 1
#         if i < j:
#             swap(arr, i, j)
#
#     swap(arr, l, j)
#     return j
#
#
# def quicksort(arr, l, r): # array, left, right
#     if l >= r: return
#     if l < r:
#         pt = partition(arr, l, r)
#         quicksort(arr, l, pt-1)
#         quicksort(arr, pt+1, r)
#
#
# n = int(input()) # number of integers
# numbers = list(map(int, input().split()))
# rawdata = numbers[::]
# answer = [0] * n
#
# quicksort(numbers, 0, n-1)
# # print(numbers)
# # print(rawdata)
#
# numbers = sorted(list(set(numbers)))
#
# for i in range(n):
#     data = rawdata[i]
#     answer[i] = numbers.index(data)
#
#
#
# print(*answer)
#
#
#
#
#
#
# ### secong trial: 위의 코드가 시간초과 나서 quicksort 버리고 일반 sort 써봄
# ### 이것도 시간초과
# n = int(input())
# numbers = list(map(int, input().split()))
# rawdata = numbers[::]
# answer = [0] * n
#
# numbers = sorted(list(set(numbers)))
#
# for i in range(n):
#     data = rawdata[i]
#     answer[i] = numbers.index(data)
#
# print(*answer)
#




### third trial:
n = int(input())
numbers = list(map(int,input().split()))
sorted_numbers = sorted(set(numbers))
data = {sorted_numbers[i]: i for i in range(len(sorted_numbers))}
answer = [data[n] for n in numbers]
print(*answer)




'''
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
'''
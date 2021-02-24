# 11004: K번째 수

n, k = map(int, input().split()) # num 수 / 찾을
arr = list(map(int, input().split()))
arr.sort()
print(arr[k-1])

"""
# 퀵정렬 써보기
def quickSort(arr, begin, end):
    if begin < end:
        p = partition(arr, begin, end)
        quickSort(arr, begin, p-1)
        quickSort(arr, p+1, end)
    return arr

def partition(arr, begin, end):
    pivot = (begin + end) // 2 # 가운데
    L = begin
    R = end
    while L < R:
        while(arr[L]<arr[pivot] and L<R): L += 1
        while(arr[R]>=arr[pivot] and L<R): R -= 1
        if L < R:
            if L == pivot: pivot = R
            arr[L], arr[R] = arr[R], arr[L]
        arr[pivot], arr[R] = arr[R], arr[pivot]

        return R # pivot

n, k = map(int, input().split()) # num 수 / 찾을
arr = list(map(int, input().split()))
res = quickSort(arr, 0, n-1)
print(res[k-1])
"""


"""
수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

"""
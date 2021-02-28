# 2231: 분해합

N = int(input())
ans = 0

for n in range(1, N+1):
    div_num = list(map(int, str(n)))
    sum_num = n + sum(div_num) # 각 자리수와 원래 수 더하기
    if(sum_num == N):
        ans = n
        break
print(ans)

# while True:
#     for n in str(N):
#         tmp += int(n)
#     if tmp == N:
#         break
#     nlist.append(tmp)
#     N = tmp
#
# print(min(nlist))

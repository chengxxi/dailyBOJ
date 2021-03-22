# 10808: 알파벳 개수

### 1
S = input()
res = [0] * 26

for st in S:
    res[ord(st) - 97] = S.count(st)

print(*res)



# ### 2
# word = list(str(input()))
# alphabet = [[alpha, 0] for alpha in 'abcdefghijklmnopqrstuvwxyz']
#
# for alpha in alphabet:
#     for character in word:
#         if alpha[0] == character:
#             alpha[1] += 1
#
# for alpha in alphabet:
#     print(alpha[1], end = ' ')



"""
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
"""
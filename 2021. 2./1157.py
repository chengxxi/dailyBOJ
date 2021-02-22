# 1157: 단어 공부

word = input().upper()
count = []

for i in set(word):
    count.append(word.count(i)) # 개수
idx = [i for i, x in enumerate(count) if x == max(count)] # 최댓값 위치 반환

if len(idx) > 1:
    print("?") # 최댓값이 여러 개
else:
    print(list(set(word))[count.index(max(count))])

"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
"""
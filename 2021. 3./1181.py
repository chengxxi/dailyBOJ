# 1181: 단어 정렬

words = []
for _ in range(int(input())):
    w = input()
    words.append((w, len(w))) # 리스트로 만들면 작동 안 함

words = list(set(words)) # 중복 제거
words.sort(key=lambda w: (w[1], w[0]))

for word in words:
    print(word[0])

print(words)


"""
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
"""
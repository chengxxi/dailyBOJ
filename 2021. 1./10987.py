# 10987: 모음의 개수

vowels = ['a', 'e', 'i', 'o', 'u']; cnt = 0
word = input()
for i in word:
    if i in vowels:
        cnt += 1
        
print(cnt)

"""
알파벳 소문자로만 이루어진 단어가 주어진다. 
이때, 모음(a, e, i, o, u)의 개수를 출력하는 프로그램을 작성하시오.
"""
# 10809: 알파벳 찾기

alphabet = "abcdefghijklmnopqrstuvwxyz"
word_list = []
word_num = []

word = str(input())

for i in word:
    word_list.append(i)

for character in alphabet:
    for i in range(len(word_list)):
        if character == word_list[i]:
            word_num.append(i)
            break
        elif i < len(word_list)-1: continue
        else:
            word_num.append(-1)
for i in word_num:
    print(i,end=" ")

"""
알파벳 소문자로만 이루어진 단어 S가 주어진다. 
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
"""
# 11721: 열 개씩 끊어 출력하기

string = input()
num = len(string)
for n in range(0, num, 10):
    print(string[n:n+10])

    
"""
알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.

한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.
"""
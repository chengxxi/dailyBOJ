# 10173: 니모를 찾아서

while True:
    string = input()
    if string == 'EOI':
        break
    string = string.lower()
    if 'nemo' in string:
        result = 'Found'
    else:
        result = 'Missing'
    print(result)

"""
영어 문장속 숨어있는 니모(Nemo)를 찾아보자. 니모를 찾는데 있어서 대소문자는 중요하지 않다.
숨겨진 니모를 찾으면 “Found”, 못찾으면 “Missing”를 각 줄에 맞게 출력하면 된다.
"""
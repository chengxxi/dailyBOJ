# 1935: 후위 표기식2

num = int(input()) # 피연산자 개수
post = input() # 후위표기식
postnums = [int(input()) for _ in range(num)] # 피연산자에 대응하는 수들

stack = []
for t in post:
    if 'A' <= t <= 'Z': # 피연산자
        stack.append(postnums[ord(t) - ord('A')])
    else:
        t1 = stack.pop()
        t2 = stack.pop()

        if t == '+':
            stack.append(t2+t1)
        elif t == '-':
            stack.append(t2-t1)
        elif t == '*':
            stack.append(t2*t1)
        elif t == '/':
            stack.append(t2/t1)

print('%.2f' % stack[0])



"""
후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.
"""
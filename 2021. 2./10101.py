# 10101: 삼각형 외우기

a=int(input())
b=int(input())
c=int(input())
if a==60 and a==b and b==c: print("Equilateral")
elif  a+b+c ==180 and (a==b or b==c or a==c): print("Isosceles")
elif a+b+c==180: print("Scalene")
else : print("Error")

"""
f = int(input())
s = int(input())
t = int(input())
sum = f + s + t
if sum == 180:
    if f == 60 and s == 60 and t == 60:
        print("Equilateral")
    if f == s or s == t or s == f:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
"""

"""
창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.

삼각형의 세 각을 입력받은 다음, 

세 각의 크기가 모두 60이면, Equilateral
세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
세 각의 합이 180이 아닌 경우에는 Error

를 출력하는 프로그램을 작성하시오.
"""
# 4153: 직각삼각형

while True:
    tri = list(map(int, input().split()))
    tri.sort()
    a, b, c = tri[0], tri[1], tri[2]        
    if c**2 == a**2 + b**2:
        if a == b == c == 0:
            break
        else:
            print("right")
            pass
    else:
        print("wrong")
    

"""
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
"""
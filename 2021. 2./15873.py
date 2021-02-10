# 15873: 공백 없는 A+B

num = str(input())
ans = 0
if len(num) == 2:		
    ans = int(num[0]) + int(num[1])
elif len(num) == 4:	#둘 다 10
    ans = 20
else:			#둘 중 하나가 10
    if int(num[-1]) == 0:		#문자열의 맨 마지막이 0, 즉 B가 10이다
        ans = int(num[0]) + 10
    else:			#중간이 0, 즉 A가 10이다
        ans = int(num[-1]) + 10
        
print(ans)

"""
자연수 A, B가 주어지면 A+B를 구하는 프로그램을 작성하시오.
자연수 A, B (0 < A, B ≤ 10)가 첫 번째 줄에 주어진다. 
단, 두 수의 사이에는 공백이 주어지지 않는다.
 두 수의 앞에 불필요한 0이 붙는 경우는 없다.
"""
# 20540: 연길이의 이상형

mbti = input()
mbtis = ["ISTJ", "ISTP", "ISFJ", "ISFP", "INTJ", "INTP", "INFJ", "INFP", 
         "ESTJ", "ESTP", "ESFJ", "ESFP", "ENTJ", "ENTP", "ENFJ", "ENFP"]
idx = mbtis.index(mbti)
rtype = mbtis[15-idx]
print(rtype)


"""
졸업을 앞둔 연길이는 크리스마스가 다가올수록 외로움을 느낀다.

그런 연길이를 위해 동우는 소개팅을 시켜주지는 않고 연길이의 이상향을 찾는 것을 도와주고자 한다.

MBTI 신봉자인 연길이는 자신과 정반대인 사람에게 매력을 느낀다. 즉, MBTI의 네가지 지표가 모두 자신과 반대인 사람이 연길이의 이상형이다.

MBTI는 다음과 같은 네 가지 척도로 성격을 표시한다. 각각의 척도는 두 가지 극이 되는 성격으로 이루어져 있다.

연길이의 이상형에 해당하는 MBTI 4글자를  대문자로 출력한다.
"""
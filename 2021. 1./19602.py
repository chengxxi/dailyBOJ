# 19602: Dog Treats

S = int(input())
M = int(input())
L = int(input())
score = S + 2 * M + 3 * L

if score < 10:
    print('sad')
else:
    print('happy')

"""
Barley the dog loves treats. At the end of the day he is either happy or sad depending on the number and size of treats he receives throughout the day. 
The treats come in three sizes: small, medium, and large. 
His happiness score can be measured using the following formula:

1 × S + 2 × M + 3 × L

where S is the number of small treats, M is the number of medium treats and L is the number of large treats.

If Barley’s happiness score is 10 or greater then he is happy. Otherwise, he is sad. 
Determine whether Barley is happy or sad at the end of the day.
"""
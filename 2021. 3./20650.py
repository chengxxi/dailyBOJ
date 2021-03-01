# 20650: Do You Know Your ABCs?

nlist = list(map(int, input().split()))
nlist.sort()
a = nlist[0]
c = nlist[-1] - a - nlist[1]
b = nlist[-1] - a - c
print(a, b, c)

"""
Farmer John's cows have been holding a daily online gathering on the "mooZ" video meeting platform. 
For fun, they have invented a simple number game to play during the meeting to keep themselves entertained.

Elsie has three positive integers A, B, and C (A<=B<=C). 
These integers are supposed to be secret, so she will not directly reveal them to her sister Bessie. 
Instead, she gives Bessie seven (not necessarily distinct) integers in the range 1, 10^9 
claiming that they are A, B, C, A+B, B+C, C+A, and A+B+C in some order.

Given a list of these seven numbers, please help Bessie determine A, B, and C. 
It can be shown that the answer is unique.
"""
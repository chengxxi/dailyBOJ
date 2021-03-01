# 20341: Moderate Pace

n = int(input())
nlist = [list(map(int, input().split())) for _ in range(3)]  # k, a, b
ans = [0] * len(nlist[0])
for i in range(len(nlist[0])):
    tmp = []
    for j in range(3):
        tmp.append(nlist[j][i])
    tmp.sort()
    ans[i] = tmp[1]


print(*ans)


"""
An ultra-marathon is a race that takes place over an uncomfortably long distance and time, typically lasting for five hours or more. 
You are part of a group of three ultra-marathon runners looking to place in this year's Great South-to-North run from Plymouth to Aberdeen.

You have a set number of days until the next race to train. You will all train together, as training alone can be dangerous. 
As everyone has their own schedule in mind for how many kilometres to run per day, this will not be easy, you will have to compromise.

The fairest option is to look at each day individually, examine the three options for how far to run, and to take the median one. 
That is to say, the option taken for each day should be one that is not be greater or lesser than both of the other possibilities at the same time.
"""
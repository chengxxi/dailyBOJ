# 4714: Lunacy
     
while True:
        weight = float(input())

        if weight < 0:
            break

        print(f'Objects weighing {weight:.2f} on Earth will weigh {(weight * 0.167):.2f} on the moon.')


# Objects weighing 100.00 on Earth will weigh 16.70 on the moon.
"""
# ㅠ제컴에선
# ㅠ되는데요
nums = list(map(float, input().split()))
for n in nums:
    if n < 0:
        break
    else:
        earth = n
        moon = round(earth/6, 2)
        print("Objects weighing %.2f on Earth will weigh %0.2f on the moon." % (earth, moon))
"""   


"""
After several months struggling with a diet, Jack has become obsessed with the idea of weighing less. 
In an odd way, he finds it very comforting to think that, if he had simply had the luck to be born on a different planet, 
his weight could be considerably less.

Of course, the planets are far out of reach, but even the Earth’s moon would yield a dramatic weight loss. 
Objects on the moon weight only 0.167 of their weight on Earth.


Input consists of one or more lines, each containing a single floating point number denoting a weight (in pounds) on the Earth. 
The end of input is denoted by a negative floating point number.


For each line of input data, your program should print a single line of the form
Objects weighing X on Earth will weigh Y on the moon.

where X is the weight from the input and Y is the corresponding weight on the moon. 
Both output numbers should be printed to a precision of 2 digits after the decimal point.
"""
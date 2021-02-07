# 5751.py

while True:
    num = int(input())
    if num <= 0:
        break
    hot = list(map(int, input().split()))
    m = hot.count(0); j = hot.count(1)
    print(f"Mary won {m} times and John won {j} times")

"""
John and Mary have been friends since nursery school. 
Since then, they have shared a playful routine: every time they meet, they play Head or Tail with a coin, and whoever wins has the privilege of deciding what they are going to play during the day. 
Mary always choose Head, and John always choose Tail.

Nowadays they are in college, but continue being truly good friends. Whenever they meet, they still play Head and Tail, and the winner decides which film to watch, or which restaurant to have dinner together, and so on.

Yesterday Mary confided to John that she has been keeping a record of the results of every play since they started, in nursery school. It came as a surprise to John! 
But since John is studying Computer Science, he decided it was a good opportunity to show Mary his skills in programming, by writing a program to determine the number of times each of them won the game over the years.

"""
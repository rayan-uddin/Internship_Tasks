# Word Order
# https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

num = int(input())

strs = []

[strs.append(input()) for i in range(num)]

print(len(Counter(strs)))
print(*list(Counter(strs).values()))
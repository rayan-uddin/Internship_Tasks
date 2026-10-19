# collections.Counter()

# https://www.hackerrank.com/challenges/collections-counter/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input()) # Number of Shoes
shoe_size = list(map(int, input().split())) # List of shoe sizes in stock
shoe_stock = Counter(shoe_size)

N = int(input()) # Number of customers
money_earned = 0

for _ in range(N):
    size, price = map(int, input().split())
    if shoe_stock[size] > 0:
        money_earned += price
        shoe_stock[size] -= 1


print(money_earned)
# Symmetric Difference

# https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
set_m = set(map(int, input().split()))

n = int(input())
set_n = set(map(int, input().split()))

diff = sorted(set_m.difference(set_n).union(set_n.difference(set_m)))

for i in diff:
  print(i)

# Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
n = set()

for i in range(m):
    n.add(input())

print(len(n))

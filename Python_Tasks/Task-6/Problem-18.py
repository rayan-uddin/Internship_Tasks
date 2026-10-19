# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

A = int(input())
a = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    command = input().split()
    values = set(map(int, input().split()))
    if command[0] == "intersection_update":
        a.intersection_update(values)
    elif command[0] == "update":
        a.update(values)
    elif command[0] == "symmetric_difference_update":
        a.symmetric_difference_update(values)
    elif command[0] == "difference_update":
        a.difference_update (values)

sum = 0

for i in a:
    sum += i
print(sum)
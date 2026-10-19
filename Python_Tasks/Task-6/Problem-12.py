# Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        value = int(command[1])
        s.remove(value)
    elif command[0] == "discard":
        value = int(command[1])
        s.discard(value)

sum = 0

for i in s:
    sum += i

print(sum)
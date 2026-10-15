# No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())
arr = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0
for i in arr:
    happiness+=int(i in a) - int(i in b)
print(happiness)
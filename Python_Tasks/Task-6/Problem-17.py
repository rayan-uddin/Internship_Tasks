# Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(map(int, input().split()))
combined = set()
for _ in range(int(input())):
    combined.add(map(int, input().split()))
print(all(a.issuperset(combined) and len(a) > len(combined) for i in combined))
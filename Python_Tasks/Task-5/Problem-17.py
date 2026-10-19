# No Idea!

# https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

len_arr, len_set = map(int, input().split())

happiness = 0

arr = input().split()

set_a = set(input().split())
set_b = set(input().split()) 

for i in arr:
    if i in set_a:
        happiness += 1
    elif i in set_b:
        happiness -= 1
    else:
        continue

print(happiness)
# Designer Door Mat
# https://www.hackerrank.com/challenges/designer-door-mat/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())
a = "WELCOME"
c = "-"
b = ".|."
b_count = 1

for i in range(n//2):
    print(f'{c * ((m - len(b * b_count)) // 2)}{b * b_count}{c * ((m - len(b * b_count)) // 2)}')
    b_count += 2
print(f'{c * ((m - len(a))//2)}{a}{c * ((m - len(a))//2)}')
b_count -=2
for i in range(n//2):
    print(f'{c * ((m - len(b * b_count)) // 2)}{b * b_count}{c * ((m - len(b * b_count)) // 2)}')
    b_count -= 2
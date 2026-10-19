# Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

for _ in range(N):
    numb = str(input())

    if re.fullmatch(r"^[789]\d*", numb) and len(numb) == 10:
        print("YES")
    else:
        print("NO")
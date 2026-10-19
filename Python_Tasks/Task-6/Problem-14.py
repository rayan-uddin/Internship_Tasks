# Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
english_students = set(map(int, input().split()))
b = int(input())
french_students = set(map(int, input().split()))

print(len(english_students.intersection(french_students)))
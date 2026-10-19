# Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
english_students = set(map(int, input().split()))
b = int(input())
french_students = set(map(int, input().split()))

print(len(english_students.union(french_students)))
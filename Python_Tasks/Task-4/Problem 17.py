# Finding the percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if n in range(2,11):
        if len(student_marks[query_name]) == 3:
            inRange = any(0 <= mark <= 100 for mark in student_marks[query_name])
            if inRange:
                averageOfName = sum(student_marks[query_name])/len(student_marks[query_name])
                print(f"{averageOfName:.2f}")
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

    marks = student_marks[query_name]

    total_sum = 0
    
    for i in marks:
        total_sum += i

    average = total_sum/len(marks)
    print(f"{average:.2f}")
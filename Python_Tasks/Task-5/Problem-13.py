# Nested Lists

# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])
        
    student_marks = sorted(set(student[1] for student in students))
    second_highest = student_marks[1]
    
    students_names = sorted(set(student[0] for student in students))
    second_highest_name = sorted(set(student[0] for student in students if student[1] == second_highest))
    
    for name in second_highest_name:
        print(name)
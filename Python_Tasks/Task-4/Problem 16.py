# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    scores = sorted({score for _, score in records})
    second_lowest_score = scores[1]
    for name in sorted(name for name, score in records if score == second_lowest_score):
        print(name)
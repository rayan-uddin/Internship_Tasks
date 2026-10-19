# Find the Runner-Up Score!

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s = set(arr)
    sorted_scores = sorted(s, reverse=True)
    print(sorted_scores[1])
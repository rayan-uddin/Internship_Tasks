# Merge the Tools!

# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for x in range(len(string) // k):

        x = string[0:k]

        y = [a for a in x]

        u = list(dict.fromkeys(y))

        print("".join(u))

        string = string[k:]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
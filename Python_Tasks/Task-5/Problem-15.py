# Lists
# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())

    l = []

    for i in range(N):
        inputs = input().split()
        method = inputs[0]

        if method == "insert":
            index = int(inputs[1])
            value = int(inputs[2])
            l.insert(index,value)

        elif method == "print":
            print(l)

        elif method == "remove":
            value = int(inputs[1])
            l.remove(value)

        elif method == "append":
            value = int(inputs[1])
            l.append(value)

        elif method == "sort":
            l.sort()

        elif method == "pop":
            l.pop()

        elif method == "reverse":
            l.reverse()
        
# sWAP cASE

# https://www.hackerrank.com/challenges/swap-case/problem

line = 'HackerRank.com presents "Pythonist 2".'

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


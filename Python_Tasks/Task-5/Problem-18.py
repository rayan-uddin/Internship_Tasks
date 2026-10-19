# The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = ["A",'E','I','O',"U"]
    stuart_score = 0
    kevin_score = 0
    length = len(string)

    for i in range(0, length):
        if string[i] in vowels:
            kevin_score += length - i
        elif string[i] not in vowels:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
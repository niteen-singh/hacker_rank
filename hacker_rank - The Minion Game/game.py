def minion_game(string):
    n = len(string)
    Stuart = 0
    Kevin = 0
    vowel = 'AEIOU'
    for i in range(n):
        if string[i] in vowel:
            Kevin += n - i
        else:
            Stuart += n - i
    if Stuart > Kevin:
        print("Stuart", Stuart)
    elif Kevin > Stuart:
        print("Kevin", Kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
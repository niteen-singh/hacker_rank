if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    for s in sorted([s[0] for s in students if (s[1] == sorted(set([s[1] for s in students]))[1])]):
        print(s)


from collections import deque

d = deque()

n = int(input())

for i in range(n):
    command, *number = input().split()

    if number:
        number = int(number[0])
        getattr(d, command)(number)

    else:
        getattr(d, command)()

print(*d)
n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

for _ in range(num_commands):
    line = input().split(" ")
    command, value = line[0], int(line[1]) if len(line) >= 2 else None

    match command:
        case 'remove':
            s.remove(value)
        case 'discard':
            s.discard(value)
        case 'pop':
            s.pop()

print(sum(s))
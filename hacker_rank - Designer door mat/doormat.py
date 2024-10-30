# Enter your code here. Read input from STDIN. Print output to STDOUT

row, col = map(int, input().split())

for i in range(1, row, +2):
    print(('.|.' * i).center(col, '-'))

print(('WELCOME').center(col, '-'))

for i in range(row - 2, 0, -2):
    print(('.|.' * i).center(col, '-'))
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

arr = []

for index in range(n):
    arr.append((index, list(map(int, input().rstrip().split()))))

k = int(input().strip())

# sort by the k-th element and maintain order using the index as a secondary key
val = sorted(arr, key=lambda x: (x[1][k], x[0]))

for _, row in val:
    print(*row)
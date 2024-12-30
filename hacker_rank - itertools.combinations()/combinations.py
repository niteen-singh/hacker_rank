from itertools import combinations

# Read input
s, k = input().split()

# Convert k to integer
k = int(k)

# Sort the string to ensure lexicographic order
s = sorted(s)

# Generate and print all combinations of lengths from 1 to k
for i in range(1, k + 1):
    for comb in combinations(s, i):
        print(''.join(comb))
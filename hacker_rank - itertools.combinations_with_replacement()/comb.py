from itertools import combinations_with_replacement

s, k = input().split()
output = list(combinations_with_replacement(sorted(s), int(k)))
for i in output:
    print(''.join(i))
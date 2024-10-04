k, m = map(int, input().split())
lists = [list(map(int, input().split()))[1:] for _ in range(k)]

possible_sums = {0}

for lst in lists:
    new_sums = set()
    for num in lst:
        for s in possible_sums:
            new_sums.add((s + num ** 2) % m)
    possible_sums = new_sums

print(max(possible_sums))
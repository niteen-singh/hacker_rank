import itertools

if __name__ == "__main__":
    S, k = input().split()

    for out in sorted(itertools.permutations(S, int(k))):
        print(*out, sep='')
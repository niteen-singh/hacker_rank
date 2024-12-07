for _ in range(int(input())):
    _ = input()
    set_A = set(map(int, input().split()))
    _ = input()
    set_B = set(map(int, input().split()))
    print(set_A.issubset(set_B))
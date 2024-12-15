n = int(input())
A = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    command = input().split()
    B = set(map(int, input().split()))
    if command[0] == "intersection_update":
        A.intersection_update(B)
    if command[0] == "update":
        A.update(B)
    if command[0] == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    if command[0] == "difference_update":
        A.difference_update(B)

print(sum(A))
a = set(map(int, input().split()))
ans = True
for i in range(int(input())):
    x = set(map(int, input().split()))
    if not a.issuperset(x):
        ans = False
        break
print(ans)
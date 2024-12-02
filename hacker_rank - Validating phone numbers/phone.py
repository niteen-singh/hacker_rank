n = int(input())
for _ in range(n):
    num = input().strip()
    if num.isdigit() and num[0] in ('7', '8', '9') and len(num) == 10:
        print("YES")
    else:
        print("NO")
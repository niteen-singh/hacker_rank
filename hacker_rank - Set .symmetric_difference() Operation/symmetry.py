el = int(input())
e = list(map(int, input().split()))[:el]
fl = int(input())
f = list(map(int, input().split()))[:fl]
print(len(list(set(e).symmetric_difference(f))))
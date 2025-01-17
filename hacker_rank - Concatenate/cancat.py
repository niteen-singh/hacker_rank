import numpy as np

n, m, p = map(int, input().split())
lst1 = []
lst2 = []

for i in range(n):
    lst1.append(list(map(int, input().split())))
for j in range(m):
    lst2.append(list(map(int, input().split())))

arr1 = np.array(lst1)
arr2 = np.array(lst2)

print(np.concatenate((arr1, arr2), axis=0))
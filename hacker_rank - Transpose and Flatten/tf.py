import numpy

n, m = map(int, input().split())
lst = []

for i in range(n):
    lst.append([*map(int, input().split())])

arr = numpy.array(lst)
print(numpy.transpose(arr))
print(arr.flatten())
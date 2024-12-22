import numpy

arr = []
n, m = map(int, input().split())
for i in range(n):
    arr.append(list(map(int, input().split())))

np_arr = numpy.array(arr)

print(numpy.max(numpy.min(np_arr, axis=1)))
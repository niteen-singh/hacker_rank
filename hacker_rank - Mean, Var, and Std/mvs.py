import numpy
N, M = map(int, input().strip().split())
my_arr = numpy.array([input().strip().split()[:M] for _ in range(N)], dtype=numpy.float_)
print(numpy.mean(my_arr, axis=1))
print(numpy.var(my_arr, axis=0))
print(round(numpy.std(my_arr, axis = None), 11))
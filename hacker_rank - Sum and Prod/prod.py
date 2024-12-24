import numpy
N, M = list(map(int, input().split()))
my_array = numpy.array([input().strip().split()[:M] for _ in range(N)], dtype=int)
print(numpy.prod(numpy.sum(my_array, axis=0)))
import numpy

z = tuple(map(int, input().split()))
print(numpy.zeros((z), dtype = int))
print(numpy.ones((z), dtype = int))
import numpy

print(round(numpy.linalg.det([list(map(float, input().split())) for i in range(int(input()))]), 2))
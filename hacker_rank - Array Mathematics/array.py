import numpy

n, m = map(int, input().split())

a = numpy.array([list(map(int, input().split())) for i in range(n)])
b = numpy.array([list(map(int, input().split())) for i in range(n)])

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
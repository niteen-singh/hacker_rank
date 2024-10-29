cube = lambda x: x**3

def fibonacci(n):
    f = []
    a, b = 0, 1
    for _ in range(n):
        f.append(a)
        a, b = b, a + b
    return f

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
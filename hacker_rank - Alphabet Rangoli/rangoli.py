def print_rangoli(size):
    alpha = [chr(i) for i in range(97, 123)]
    alpha = alpha[:size]
    indices = list(range(size))
    indices = indices[:-1] + indices[::-1]
    for i in indices:
        s_index = i + 1
        orignal = alpha[-s_index:]
        rev = orignal[::-1]
        row = rev + orignal[1:]
        row = "-".join(row)
        width = size * 4 - 3
        print(row.center(width, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
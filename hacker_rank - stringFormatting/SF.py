def print_formatted(number):
    # Determine the width for formatting based on the largest number
    width = len(bin(number)) - 2  # Subtracting 2 for the '0b' prefix

    for i in range(1, number + 1):
        # Formatting and printing each number
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)  # Remove '0o' prefix
        hexadecimal = hex(i)[2:].upper().rjust(width)  # Remove '0x' prefix and capitalize
        binary = bin(i)[2:].rjust(width)  # Remove '0b' prefix

        print(f"{decimal} {octal} {hexadecimal} {binary}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
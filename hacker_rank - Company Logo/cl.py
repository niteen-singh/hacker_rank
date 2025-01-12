if __name__ == '__main__':
    s = input().strip()
    char_counts = {}

    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    sorted_characters = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))

    for char, count in sorted_characters[:3]:
        print(char, count)
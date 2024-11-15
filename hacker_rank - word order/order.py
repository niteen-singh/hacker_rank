n = int(input())
words = [input().strip() for _ in range(n)]

word_count = {}
order_of_appearance = []

for word in words:
    if word not in word_count:
        word_count[word] = 1
        order_of_appearance.append(word)
    else:
        word_count[word] += 1

print(len(word_count))

print(" ".join(str(word_count[word]) for word in order_of_appearance))
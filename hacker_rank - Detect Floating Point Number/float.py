import re

num_test = int(input())
pattern = re.compile(r'[-+]?\d*\.\d+')

for _ in range(num_test):
    print(bool(pattern.fullmatch(input())))
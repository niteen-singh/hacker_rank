import re

t = int(input())
pattern = r'^(?=.*[A-Z]{2})(?=.*[0-9]{3})(?!.*(.)\1)[a-zA-Z0-9]{10}$'

for _ in range(t):
    string = ''.join(sorted(input()))
    result = re.match(pattern, string)

    print('Valid' if result else 'Invalid')
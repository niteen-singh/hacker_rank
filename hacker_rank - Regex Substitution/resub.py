import re

pattern = r'(?<= )(&&|\|\|)(?= )'
replacement = lambda m: 'and' if m.group(0) == '&&' else 'or'

for i in range(int(input())):
    s = input()
    print((re.sub(pattern, replacement, s)))
import re
print((lambda m: m and m.group(1) or -1)(re.search(r'([0-9a-zA-Z])\1+', input())))
import re

S = input()
k = input()

i = 0

while i < len(S) - 1:

    m = re.search(k, S[i:])

    if not m:
        if i ==0:
            print((-1, -1))
        break

    elif m:
        print((m.start()+i, m.end()+i-1))
        i += m.end() - 1 if len(k)!=1 else m.end()
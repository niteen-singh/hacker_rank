# It works in pypy3 but not in python3
import re
T =int(input())
for x in range(T):
    S = input()
    try:
        if re.compile(S):
            print("True")
    except:
        print("False")
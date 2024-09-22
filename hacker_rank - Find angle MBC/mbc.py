# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
def mbc(AB, BC):
    return f"{math.degrees(math.atan(AB / BC)):.0f}\u00b0"

if __name__ == "__main__":
    print(mbc(10, 10))
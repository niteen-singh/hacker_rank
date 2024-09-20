import math
import os
import random
import re
import sys
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    dt1, dt2 = [datetime.strptime(x, '%a %d %b %Y %H:%M:%S %z') for x in [t1, t2]]
    return str(abs(int((dt1 - dt2).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

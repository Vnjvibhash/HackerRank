#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#


def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    s = list()
    len_s = len(values)
    for i in range(len_s):
        s += [values[i]]*freqs[i]
    s.sort()
    middle = sum(freqs)//2
    if middle % 2 == 0:
        Low = s[:middle]
        Upper = s[middle:]
    else:
        Low = s[:middle-1]
        Upper = s[middle+1:]
    Q1 = statistics.median(Low)
    Q3 = statistics.median(Upper)
    print(round((Q3-Q1), 1))


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)

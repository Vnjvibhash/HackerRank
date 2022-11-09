#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    total = sum(vals)
    mean = (total/n)
    arr = []
    for i in range(n):
        arr.append((vals[i]-mean)**2)
    print(round((math.sqrt(sum(arr)/n)), 1))


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def quartiles(arr, level):
    # Write your code here
    arr = sorted(arr) if level == 0 else arr
    odd = True if len(arr) % 2 != 0 else False
    idx_q2 = ((len(arr)+1)/2)-1
    res = []
    level += 1
    if level == 2:
        if odd:
            return int(arr[int(idx_q2)])
        else:
            return int((arr[int(idx_q2)]+arr[int(math.ceil(idx_q2))])/2)
    else:
        if odd:
            res.append(quartiles(arr[:int(idx_q2)], level))
            res.append(arr[int(idx_q2)])
            res.append(quartiles(arr[int(idx_q2+1):], level))
        else:
            res.append(quartiles(arr[:int(math.ceil(idx_q2))], level))
            res.append(quartiles(arr, level))
            res.append(quartiles(arr[int(math.ceil(idx_q2)):], level))
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data, 0)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

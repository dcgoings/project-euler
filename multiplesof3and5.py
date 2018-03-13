import math
from functools import reduce
import operator

"""

Find the sum of all multiples of 3 and 5 below 1000.

"""

def multiplesof3and5(num):
    result = 0
    for i in range(num):
        if (i % 3 == 0) or (i % 5 == 0):
            result += i
            print("Adding %s to result. Now %s." % (i, result))

multiplesof3and5(1000)

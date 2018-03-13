import math
from functools import reduce
import operator

"""

Fibonacci = 0 1 1 2 3 5 8 13 21 34 55 89 ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""

def evenfibs():
    x = 1
    y = 2
    result = 2
    while (x < 4000000) and (y < 4000000):
        x = (x + y)
        print("X equals %s" % x)
        y = (x + y)
        print("Y equals %s" % y)
        if (x > 4000000 or y > 4000000):
            break

        if (x % 2 == 0):
            print("adding %s to result" % x)
            result += x
        if (y % 2 == 0):
            result += y
            print("adding %s to result" % y)
        print("Result: %s " % result)

evenfibs()

import math
from functools import reduce
import operator

"""

The difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

def sumsquarediff():
    sumofsq = 0
    sqofsum = 0
    sqofsumfinal = 0
    y = 0
    for x in range(1,101):
        print("Currently on %s^2 = %s" % (x, sumofsq))
        print("Adding %s to %s" % (x, sqofsum))
        y = (x*x)
        sumofsq += y
        sqofsum += x

    sqofsumfinal = sqofsum*sqofsum
    print("%s^2 = %s" % (sqofsum, sqofsumfinal))
    result = (sqofsumfinal - sumofsq)
    print (result)

sumsquarediff()

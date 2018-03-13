import math
from functools import reduce
import operator

"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

def prime10001(n):

    length = n * 1000
    # print (length)
    allnums = math.floor(length) * [True]
    count = 0
    listofprimes = []

    for x in range (2, length):
        if allnums[x] == True:
            listofprimes.append(x)
            print("%s is prime!" % x)
            # print (listofprimes)
            count += 1
            if count == n:
                print ("%s is the %s prime number!" % (x, n))
                return x
            for y in range(x*2, length, x):
                allnums[y] = False

prime10001(10001)

import math
from functools import reduce
import operator

"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

def smallestmultiple():
    bool = False
    count = 1
    num = 20
    mults = [11,12,13,14,15,16,17,18,19,20]
    while bool == False:
        for x in mults:
            # print ("testing %s / %s" % (num, x))
            if num % x == 0:
                count+=1
                # print ("count: %s" %count)

            else:
                count = 1
                num += 20
                break
        if count == 10:
            bool = True
            return (num)
            break

smallestmultiple()

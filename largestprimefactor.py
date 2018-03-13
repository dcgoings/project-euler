import math
from functools import reduce
import operator

"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def largestprimefactor(num):
    sq = math.sqrt(num)
    factor = 2
    setOfFactors = set()
    listOfFactors = []

    while factor < sq:
        while num % factor == 0:
            num = num / factor
            print (num)
            setOfFactors.add(factor)
            listOfFactors.append(factor)
        factor+=1
    print (listOfFactors)
    print (setOfFactors)

largestprimefactor(600851475143)

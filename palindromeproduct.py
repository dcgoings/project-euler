import math
from functools import reduce
import operator

"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def palindromeproduct():
    x = 100
    y = 100
    z = 0
    largest = 0

    for x in range(100, 999):
        for y in range(100, 999):
            z = x * y
            split = [int(d) for d in str(z)]
            split2 = [int(d) for d in str(z)]
            split2.reverse()

            if (split == split2) and (z > largest):
                largest = z
                print ("new largest: %s" % largest)
            y+=1
        x+=1

palindromeproduct()

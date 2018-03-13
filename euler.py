import math
from functools import reduce
import operator

def multiplesof3and5(num):
    result = 0
    for i in range(num):
        if (i % 3 == 0) or (i % 5 == 0):
            result += i
            print("Adding %s to result. Now %s." % (i, result))

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
        print(result)

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

def smallestmultiple():
    bool = False
    count = 1
    num = 20
    mults = [11,12,13,14,15,16,17,18,19,20]
    while bool == False:
        for x in mults:
            print ("testing %s / %s" % (num, x))
            if num % x == 0:
                count+=1
                print ("count: %s" %count)

            else:
                count = 1
                num += 20
                break
        if count == 10:
            bool = True
            return (num)
            break

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

def largestproductinseries():
    s=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

    digits = [int(d) for d in str(s)]
    runningcount = 1
    largest = 0
    temp = []
    for x in digits:
        runningcount+=1
        if runningcount == 990:
            break

        temp = digits[:13]
        if 0 not in temp:
            print ("\nCalculating product of series: %s" % temp)
            v = reduce(operator.mul, temp)
            print ("Product is %s" % v)
            if v > largest:
                print("New product %s > %s" % (v, largest))
                largest = v
            temp = []
        digits = digits[1:]
    print (largest)
    
    # multiplesof3and5(1000)
    # evenfibs()
    # largestprimefactor(60085147514)
    # largestprimefactor(18)
    # largestprimefactor(13195)
    # palindromeproduct()
    # smallestmultiple()
    # sumsquarediff()
    # prime10001(410)
    # largestproductinseries()

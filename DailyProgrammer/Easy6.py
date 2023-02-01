import math
from decimal import *

#Factorial is just n * (n-1) * (n-2) * (n - 3)... So we can do a bit of recursion on this
def findFactorial(number):
    if number == 0:
        return 1
    else:
        return number * findFactorial(number - 1)

def findPi():
    
    #We need a sum since the algoritum calls for the sum of n -> infinity
    totalSum = Decimal(0)
    #This could be moved into a for loop but I assume that like other algoritums for PI we are actually dependent
    #On the sum to be concidered done
    count = 0
    #We can precalculte this since for every interaction this value stays constant.
    constantMulti = (pow(2,(3/2)))/9801

    while True:
        sumForN = constantMulti * (((findFactorial(4 * count)) / (pow(findFactorial(count),4))) * (((26390 * count) + 1103) / (pow(396,(4*count)))))
        totalSum += Decimal(sumForN)

        if(abs(sumForN) < 1e-30):
            break

        count += 1
    
    context = Context(prec=50)
    setcontext(context)
    print("The value of pi to 30 places is: " + str((1/totalSum)))

findPi()
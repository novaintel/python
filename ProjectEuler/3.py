#For 600851475143 the largest number is 6857.0

def primeFactor(number):
    #Might as well keep a list of all prime numbers we found
    factors=[]

    #This is the factor we will always check againts
    primeCheck=2

    while number > 1:
        #A prime number is a factor of one and itself. Modules returns what is left over from a devide which for a prime number
        #Would be 0!
        while number % primeCheck == 0:
            #Since we found a prime element lets store it
            factors.append(primeCheck)
            #Not sure about this. We are reducing the range we have to search
            number /= primeCheck
        #Again not fully sure on this
        primeCheck += 1

    return factors

pfs = primeFactor(600851475143)
print(max(pfs))



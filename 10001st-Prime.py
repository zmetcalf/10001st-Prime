import math

counter = 0
primes = 1

def CheckPrime(numCheck):
    i = 2
    maxCheck = math.sqrt(numCheck)
    while i <= maxCheck:
        if numCheck % i == 0:
            return 0
        i += 1
    return 1
    
while counter < 10001:
    primes += 1
    if CheckPrime(primes):
        counter += 1
    
print primes
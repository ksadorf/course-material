import random
import fractions


def dicho_iter_mod(x, y, mod):
    result = 1
    while y != 0:
        if y & 1 == 1:  # si y impair
            result *= x
            result = result % mod
            y -= 1
        else:  # y est pair
            x *= x
            x = x % mod
            y >>= 1
    return result


def isBigPrime(n, k):
    if(n % 2 == 0):
        return False

    # Test probabiliste
    # print "Test probabiliste sur ",n
    for i in range(0, k):
        a = random.randint(2, n - 1)
        if(fractions.gcd(a, n) != 1):
            return False
        if(dicho_iter_mod(a, n-1, n) != 1):
            return False
    # print ""
    # Si le test est bon on a soit un nombre premier
    # soit un nombre de carmichael // peut probable avec k grand
    # Dans les deux cas on peut utiliser l'algo du RSA
    return True

test = 100000000
while(not isBigPrime(test, 20)):
    test += 1
print(test)

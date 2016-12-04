from random import *


def generate_encryption_key(prime):
    while True:
        num = randint(1,prime)
        if gcd(num,prime) == 1:
            return num

def generate_decryption_key(prime,e):
    for d in range(1, prime):
        if ( ( (e * d) % prime ) == 1 ):
            return d

def encrypt(data, key, prime):
    return pow(data, key, prime)

def decrypt(data, key, prime ):
    return pow(data, key, prime)


def gcd(x,y):
    while x != y:
        if x > y:
            return gcd(x-y,y)
        else:
            return gcd(x,y-x)
    return x

def generate_keys(prime):
    while True:
        e = generate_encryption_key(prime-1)
        d = generate_decryption_key(prime-1,e)
        if d != None:
            return e,d
def isPrime(Number):
    return 2 in [Number,2**Number%Number]

def generate_prime(p,q):
    primes = [i for i in range(p,q) if isPrime(i)]
    return choice(primes)

#test
"""
prime = 73
e,d = generate_keys(prime)
print(e,d)
data = 5
en = encrypt(data, e, prime)
de = decrypt(en, d, prime)
print(data, en, de)"""


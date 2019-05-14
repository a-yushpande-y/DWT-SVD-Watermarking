import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
   e=e%phi
   for x in range(1,phi):
       if((e*x)%phi==1):
           return x
   return 1


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
   
    n = p * q

    phi = (p-1) * (q-1)


    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)


    d = multiplicative_inverse(e, phi)
    

    return ((e, n), (d, n))

def encrypt(plaintext):
    print
    print "For RSA"
    p = int(raw_input("Enter a prime number "))
    q = int(raw_input("Enter another prime number (Diffrent than previous one):"))
    public, private = generate_keypair(p, q)
    print " public key is ", public ," private key is ", private
    key, n = private
    cipher = [(ord(char) ** key) % n for char in plaintext]
    f = open("rsain.txt", "w")
    for i in cipher:
        f.write(str(i))
        f.write("\n")
    print "encrypted message is: "
    print ''.join(map(lambda x: str(x), cipher))

def decrypt(ciphertext):

    print "For RSA"
    key = int(raw_input("Enter public key "))
    n = int(raw_input("Enter n"))
    plain = [chr((char ** key) % n) for char in ciphertext]
    print "Decrypted message is "
    print ''.join(plain)
    return ''.join(plain)

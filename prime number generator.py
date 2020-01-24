from math import sqrt
count = int(input("how many prime numbers do you want to make? "))
            
def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True
def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n
generator = prime_generator()

for i in range(count):
    count2 = i+1
    gen = next(generator)
    print("{0}: {1}".format(count2, gen))

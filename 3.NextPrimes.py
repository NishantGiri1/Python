import math


def generate_primes(n):
    primes_array = []
    current = 2
    while len(primes_array) < n:
        is_prime = True
        for i in range(2, int(math.sqrt(current)) + 1):
            if current % i == 0:
                is_prime = False
                break
        if is_prime:
            primes_array.append(current)
        current += 1
    return primes_array


print(generate_primes(5))

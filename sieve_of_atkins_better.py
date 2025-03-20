def sieve(limit):
    if limit < 2:
        return []
    res = [False] * (limit + 1)
    if limit >= 2:
        res[2] = True
    if limit >= 3:
        res[3] = True

    for x in range(1, int(limit**0.5) + 1):
        for y in range(1, int(limit**0.5) + 1):
            n = 4 * x * x + y * y
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                res[n] = not res[n]
            n = 3 * x * x + y * y
            if n <= limit and n % 12 == 7:
                res[n] = not res[n]
            n = 3 * x * x - y * y
            if x > y and n <= limit and n % 12 == 11:
                res[n] = not res[n]

    for n in range(5, int(limit**0.5) + 1):
        if res[n]:
            for k in range(n * n, limit + 1, n * n):
                res[k] = False

    primes = [2, 3] + [n for n in range(5, limit + 1) if res[n]]
    return primes

def pick_prime(primes, min_size=1000):
    for prime in primes:
        if prime >= min_size:
            return prime
    return primes[-1]

def hash(string, modulus):
    hash_value = 5381
    for char in string:
        hash_value = ((hash_value << 5) + hash_value) ^ ord(char)
    return hash_value % modulus

if __name__ == '__main__':
    primes = sieve(10000)
    modulus = pick_prime(primes, 1000)

    test_array = ["alpha", "beta", "gamma", "delta", "epsilon"]

    for string in test_array:
        hash_value = hash(string, modulus)
        print(f"Hash of {string} is {hash_value}")
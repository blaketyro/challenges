# https://projecteuler.net/problem=5

"""
It's almost easier to do this on paper using the fundamental theorem of arithmetic:

Write down all the prime factorizations of 2-20:
(don't need 1 since any number will be divisible by it)
2  = 2^1 
3  = 3^1
4  = 2^2
5  = 5^5
6  = 2^1 * 3^1
7  = 7^1
8  = 2^3
9  = 3^2
10 = 2^1 * 5^1
11 = 11^1
12 = 2^2 * 3^1
13 = 13^1
14 = 2^1 * 7^1
15 = 3^1 * 5^1
16 = 2^4
17 = 17^1
18 = 2^1 * 9^1
19 = 19^1
20 = 2^2 * 5^1

The largest exponent for any particular prime factor (e.g. 4 for 2 with 16 = 2^4) will be the exponent of that prime
factor in the answer number, because it needs to be divisible by the prime that many times.

So it's simple enough to read of the answer:
2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232792560
"""
import math
from collections import Counter
from p3 import is_prime

print(2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)

# A general programmatic solution with the same idea would be:


def prime_factorization(n):
    factorization = Counter()
    for p in range(2, n+1):
        if n % p == 0 and is_prime(p):  # this feels inefficient?
            d = n
            factorization[p] = 0
            while d % p == 0:
                d //= p
                factorization[p] += 1
    return factorization


def solve(n=20):
    factorization = Counter()
    for i in range(2, n+1):
        for p, e in prime_factorization(i).items():
            factorization[p] = max(e, factorization[p])
    answer = math.prod(p ** e for p, e in factorization.items())
    print(answer)


solve()

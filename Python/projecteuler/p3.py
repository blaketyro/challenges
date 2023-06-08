# https://projecteuler.net/problem=3

from functools import cache


@cache
def is_prime(n):
    if n % 2 == 0:
        return n == 2
    # if n wasn't divisible by 2, then it can't be divisible by even, so skip those
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def largest_prime_factor(n):
    # start from the bottom and divide to find the big factors quicker
    for small_factor in range(2, n):
        if n % small_factor == 0:
            big_factor = n // small_factor
            if is_prime(big_factor):
                return big_factor
    # there's surely f


def solve():
    print(largest_prime_factor(600851475143))


if __name__ == "__main__":
    solve()

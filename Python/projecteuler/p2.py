# https://projecteuler.net/problem=2

def solution1(limit=4000000):
    total = 0
    a, b = 0, 1
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total


def solve():
    print(solution1())


solve()

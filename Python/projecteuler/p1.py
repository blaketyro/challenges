# https://projecteuler.net/problem=1


# Specific looping solution
def solution1(limit=1000):
    return sum(i for i in range(1, limit) if i % 3 == 0 or i % 5 == 0)


# This problem can also be solved mathematically in constant time. Take n to be the max number to consider (limit - 1).
# Then ~n/3 of the numbers will be multiples of 3, and their sum will just be the triangular number sequence times 3.
# Same idea for 5, just this will double count multiples of 3 and 5 (aka 15), so subtract those off.

# Constant time math solution
def solution2(limit=1000):
    n = limit - 1
    def tri(n): return n * (n + 1) // 2  # could use lambdas here but not recommended
    def helper(d): return d * tri(n // d)  # https://peps.python.org/pep-0008/#programming-recommendations
    return helper(3) + helper(5) - helper(15)


# General looping solution
def solution3(limit=1000, nums=(3, 5)):
    total = 0
    for i in range(1, limit):
        if any(i % n == 0 for n in nums):
            total += i
    return total


def solve():
    print(solution1(10))
    print(solution1())
    print(solution2(10))
    print(solution2())
    print(solution3(10))
    print(solution3())


solve()

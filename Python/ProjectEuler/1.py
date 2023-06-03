# https://projecteuler.net/problem=1

# General solver
def sum_multiples(below=10, nums=(3, 5)):
    total = 0
    for i in range(1, below):
        if any(i % n == 0 for n in nums):
            total += i
    return total

print(sum_multiples())
print(sum_multiples(1000))

# Specific solver
def solve(below=10):
    return sum(i for i in range(1, below) if i % 3 == 0 or i % 5 == 0)

print(solve())
print(solve(1000))

# This problem can also be solved mathematically. Take n to be the max number to consider (below - 1).
# Then ~n/3 of the numbers will be multiples of 3, and their sum will just be the triangular number sequence times 3.
# Same idea for 5, just this will double count multiples of 3 and 5 (aka 15), so subtract those off.

def tri(n):
    return n * (n + 1) // 2
def helper(n, d):
    return d * tri(n//d)
def solve2(below=10):
    n = below - 1
    helper = lambda d: d * tri(n // d)
    return helper(3) + helper(5) - helper(15)

print(solve2())
print(solve2(1000))

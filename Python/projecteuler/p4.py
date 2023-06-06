# https://projecteuler.net/problem=4


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def solve():
    answer = 0
    for a in range(999, 99, -1):
        for b in range(999, a - 1, -1):
            if is_palindrome(a * b):
                answer = max(answer, a*b)
    print(answer)


solve()

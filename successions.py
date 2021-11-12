def fibonacci_rec(n: int) -> int:
    """
    Returns the n term of the fibonacci numbers using a pure recursive approach
    :param n: term to calculate
    :return: n term of the fibonacci sequence
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter(n: int) -> int:
    """
    Returns the n term of the fibonacci numbers using an iterative approach
    :param n: term to calculate
    :return: n term of the fibonacci sequence
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fibonacci_dynamic(n: int) -> int:
    """
    Returns the n term of the fibonacci numbers using a dynamic programming approach

    :param n: term to calculate
    :return: n term of the fibonacci sequence
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[n]


def fibonacci_direct(n: int) -> int:
    """
    Returns the n term of the fibonacci numbers using the direct formula

    :param n: term to calculate
    :return: n term of the fibonacci sequence
    """
    return round(((1 + 5 ** 0.5) / 2) ** n / 5 ** 0.5)


def prime_generator(limit: int) -> int:
    """
    Use the Eratosthenes crib to generate prime numbers

    :param limit: upper limit of the prime numbers to generate
    :return: Each time is called return the next prime number
    """
    primes = [True] * limit
    primes[0] = False
    primes[1] = False
    for i in range(2, limit):
        if primes[i]:
            for j in range(i * i, limit, i):
                primes[j] = False
    for i in range(limit):
        if primes[i]:
            yield i


def binary_exponentiation(n: int, k: int) -> int:
    """
    Calculate the k-th power of n using the binary exponentiation algorithm

    :param n: base
    :param k: exponent
    :return: n^k
    """
    if k == 0:
        return 1
    if k == 1:
        return n
    if k % 2 == 0:
        return binary_exponentiation(n * n, k // 2)
    else:
        return n * binary_exponentiation(n * n, k // 2)


def superfactorial(n: int) -> int:
    """
    Calculate the super factorial n

    :param n: number to calculate the super factorial using the following recursion
    binary_exponential(n,n)*superfactorial(n-1)
    :return: super factorial of n
    """
    if n == 0:
        return 1
    return binary_exponentiation(n, n) * superfactorial(n - 1)



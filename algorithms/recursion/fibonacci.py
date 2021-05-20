from functools import lru_cache

@lru_cache                          #This improves run time dramatically by using a little more memory
def fib(n):
    if n == 1:
        return 0
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def getFibSeq(n):

    for x in range(1, n+1):
        yield fib(x)


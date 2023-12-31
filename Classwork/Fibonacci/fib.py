from functools import lru_cache


# Числа Фибоначчи (попробуйте убрать lru_cache) :)

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(100)])
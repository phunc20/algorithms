"""
01. What is tail-recursive in this case? Will it help perforamnce?
02. Comparision
    In [6]: import fibo
    
    In [7]: %timeit fibo.fibo_dyn(10)
    9.91 µs ± 283 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    
    In [8]: %timeit fibo.fibo_recur(10)
    21.4 µs ± 20.3 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    
    In [9]: %timeit fibo.fibo_recur(10)
    21.6 µs ± 61.9 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    
    In [10]: %timeit fibo.fibo_dyn(10)
    9.65 µs ± 13.2 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

    In [11]: %timeit fibo.fibo_dyn2(10)
    731 ns ± 4.05 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
"""

def fibo_recur(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibo_recur(n-1) + fibo_recur(n-2)

def fibo_dyn(n):
    import numpy as np
    cache = np.ones(n+1, dtype=np.uint64)
    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

def print_fib_lt(n):
    """
    This is the function on the official website of Python

    return a fibonacci number close to n
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fibo_dyn2(n):
    """
    return
      the n-th fibonacci number
    """
    if n < 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(1,n):
            a, b = b, a+b
        return b

if __name__ == "__main__":
    import time
    t0 = time.time()
    print(f"fibo_recur(100)={fibo_recur(100)}")
    t1 = time.time()
    print(f"Took {t1-t0}s")
    print()
    t0 = time.time()
    print(f"fibo_dyn(100)={fibo_dyn(100)}")
    t1 = time.time()
    print(f"Took {t1-t0}s")








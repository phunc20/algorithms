"""
In [2]: %timeit fib_append(100_000)
762 ms ± 584 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [3]: %timeit fib_reserve(100_000)
760 ms ± 1.17 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [4]: %timeit fib_reserve(100_000)
759 ms ± 802 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [5]: %timeit fib_append(100_000)
762 ms ± 1.29 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [6]: %timeit fib_append(100_000)
761 ms ± 663 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [7]: %timeit fib_append(1_000)
247 µs ± 1.07 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [8]: %timeit fib_reserve(1_000)
313 µs ± 550 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [9]: %timeit fib_append(1_000)
249 µs ± 927 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [10]: %timeit fib_reserve(1_000)
319 µs ± 4.65 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [11]: %timeit fib_append(1_000)
255 µs ± 1.13 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
"""


def fib_reserve(n):
    assert n >= 0
    if n == 0:
        return 0
    elif n == 1 or n ==2:
        return 1

    fibos = [1] * (n+1)
    for i in range(3, n+1):
        fibos[i] = fibos[i-1] + fibos[i-2]
    return fibos[n]


def fib_append(n):
    assert n >= 0
    if n == 0:
        return 0
    elif n == 1 or n ==2:
        return 1

    fibos = [1] * 3
    for i in range(3, n+1):
        new_member = fibos[-1] + fibos[-2]
        fibos.append(new_member)
    return fibos[n]







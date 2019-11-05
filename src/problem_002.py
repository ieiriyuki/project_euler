#!/usr/bin/env python

from logging import getLogger
logger = getLogger(__name__)


def main():
    limit = 4 * 10 ** 6
    fibos = [1, 2]
    evens = [2]

    n = 1
    current = fibos[n]

    while current <= limit:
        current += fibos[n - 1]
        if current > limit:
            break
        fibos += [current]
        n += 1
        if n % 3 == 1:
            evens += [current]

    print("fibo_n-1: {}, even_n-1: {}, sum: {}".format(
        fibos[n], evens[-1], sum(evens)))
    return 1


def fibo(n):
    n = int(n)
    x1 = 1
    x2 = 2
    answer = 0
    if n == 1:
        return x1
    elif n == 2:
        return x2
    else:
        answer = fibo(n - 1) + fibo(n - 2)

    return answer


if __name__ == "__main__":
    main()

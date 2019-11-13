#!/usr/bin/env python


from tqdm import tqdm


NUMBER = 600851475143
MAX_PRIME = 71
UPPER = NUMBER // MAX_PRIME


def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
              31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    mp = MAX_PRIME
    limit = 775001
    print(NUMBER, limit * limit, UPPER, limit)

    if NUMBER < limit * limit or UPPER < limit:
        return 0

    for i in tqdm(range(73, limit, 2)):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        else:
            continue

        if check_dividable(i):
            mp = i

    print(mp)  # 6857

    return 1


def check_dividable(i):
    if UPPER % i == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

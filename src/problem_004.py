#!/usr/bin/env python


def main():
    MAX = 999
    MIN = 100
    par = 0
    for i in range(MAX, MIN + 1, -1):
        for j in range(MAX - 1, MIN, -1):
            num = i * j
            num_str = str(num)
            # print(num_str)
            if check_palindromic(num_str) and num > par:
                par = num

    print(par)

    return 1


def check_palindromic(num_str):
    n = len(num_str) // 2

    seq1 = num_str[:n]
    seq2 = "".join([num_str[-x] for x in range(1, n + 1)])
    # print(seq1, seq2)

    return seq1 == seq2



if __name__ == "__main__":
    main()

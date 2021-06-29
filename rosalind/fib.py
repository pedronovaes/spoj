import sys


def rabbit_pairs(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rabbit_pairs(n - 1, k) + k * rabbit_pairs(n - 2, k)


if __name__ == '__main__':
    seq = sys.stdin.read().split(' ')
    n = int(seq[0])
    k = int(seq[1])

    total = rabbit_pairs(n=n, k=k)
    print(total)

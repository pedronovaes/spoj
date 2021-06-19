import sys


def hamming_distance(s1, s2):
    dh = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dh += 1

    return dh


if __name__ == '__main__':
    dnas = sys.stdin.read().split('\n')
    dh = hamming_distance(dnas[0], dnas[1])
    print(dh)

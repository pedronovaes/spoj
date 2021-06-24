import sys


def find_motif(s, t):
    pos = ''

    for i in range(len(s) - len(t)):
        sub = s[i:i + len(t)]

        if sub == t:
            pos = pos + str(i + 1) + ' '

    return pos[:-1]


if __name__ == '__main__':
    dnas = sys.stdin.read().split('\n')
    pos = find_motif(s=dnas[0], t=dnas[1])

    print(pos)

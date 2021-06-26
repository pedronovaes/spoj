import sys
import re


def transition_transversion_ratio(s1, s2):
    ts = 0
    tv = 0

    for i in range(len(s1)):
        if ((s1[i] == 'A') and (s2[i] == 'T')) or ((s1[i] == 'T') and (s2[i] == 'A')):  # A <-> T
            tv += 1
        elif ((s1[i] == 'A') and (s2[i] == 'C')) or ((s1[i] == 'C') and (s2[i] == 'A')):  # A <-> C
            tv += 1
        elif ((s1[i] == 'G') and (s2[i] == 'C')) or ((s1[i] == 'C') and (s2[i] == 'G')):  # G <-> C
            tv += 1
        elif ((s1[i] == 'G') and (s2[i] == 'T')) or ((s1[i] == 'T') and (s2[i] == 'G')):  # G <-> T
            tv += 1
        elif ((s1[i] == 'A') and (s2[i] == 'G')) or ((s1[i] == 'G') and (s2[i] == 'A')):  # A <-> G
            ts += 1
        elif ((s1[i] == 'T') and (s2[i] == 'C')) or ((s1[i] == 'C') and (s2[i] == 'T')):  # T <-> C
            ts += 1

    ratio = ts / tv

    return round(ratio, 11)


if __name__ == '__main__':
    dnas = ''.join(sys.stdin.read().split('\n'))
    dnas = re.split(pattern='>Rosalind_[0-9]+', string=dnas)[1:]

    tstv_ratio = transition_transversion_ratio(s1=dnas[0], s2=dnas[1])
    print(tstv_ratio)

import sys
import re
import numpy as np


def consensus(dna):
    m = []
    for i in dna:
        temp = [j for j in i]
        m.append(temp)
    m = np.matrix(m)

    A, C, G, T = [], [], [], []

    for col in range(m.shape[1]):
        temp, = np.array(m[:, col].T)
        A.append(np.count_nonzero(temp == 'A'))
        C.append(np.count_nonzero(temp == 'C'))
        G.append(np.count_nonzero(temp == 'G'))
        T.append(np.count_nonzero(temp == 'T'))

    profile = np.matrix([A, C, G, T])

    consensus_string = ''

    for col in range(profile.shape[1]):
        temp, = np.array(profile[:, col].T)
        max = np.argmax(temp)

        if max == 0:  # A is the most recurrent
            consensus_string += 'A'
        elif max == 1:  # C is the most recurrent
            consensus_string += 'C'
        elif max == 2:  # G is the most recurrent
            consensus_string += 'G'
        elif max == 3:  # T is the most recurrent
            consensus_string += 'T'

    print(consensus_string)
    print('A:', ' '.join(str(i) for i in A))
    print('C:', ' '.join(str(i) for i in C))
    print('G:', ' '.join(str(i) for i in G))
    print('T:', ' '.join(str(i) for i in T))

    return consensus_string


if __name__ == '__main__':
    FASTA = sys.stdin.read().replace('\n', '')
    FASTA = re.split(pattern='>Rosalind_[0-9]+', string=FASTA)[1:]

    cs = consensus(dna=FASTA)

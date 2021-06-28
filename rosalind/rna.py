import sys


def dna_to_rna(dna):
    rna = dna.replace('T', 'U')

    return rna


if __name__ == '__main__':
    dna = sys.stdin.read()

    rna = dna_to_rna(dna)
    print(rna)

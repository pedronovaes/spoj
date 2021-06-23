import sys
import re

CODON_TABLE = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'C': ['UGU', 'UGC'],
    'D': ['GAU', 'GAC'],
    'E': ['GAA', 'GAG'],
    'F': ['UUU', 'UUC'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'H': ['CAU', 'CAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'K': ['AAA', 'AAG'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'M': ['AUG'],
    'N': ['AAU', 'AAC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'Q': ['CAA', 'CAG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'W': ['UGG'],
    'Y': ['UAU', 'UAC'],
    'STOP': ['UAA', 'UAG', 'UGA']
}


def rna_to_protein(rna):
    prot = ''

    # Separating the rna into codons
    codons = re.findall(pattern='.{1,3}', string=rna)

    for codon in codons:
        for aminoacid in CODON_TABLE:
            if codon in CODON_TABLE[aminoacid]:
                if aminoacid != 'STOP':
                    prot += aminoacid
                else:  # Stop the translation step
                    break

    return prot


if __name__ == '__main__':
    rna = sys.stdin.read()
    prot = rna_to_protein(rna)
    print(prot)

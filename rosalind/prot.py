import sys
import re

CODON_TABLE = {
    'F': ['UUU', 'UUC'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'Y': ['UAU', 'UAC'],
    'C': ['UGU', 'UGC'],
    'W': ['UGG'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'H': ['CAU', 'CAC'],
    'Q': ['CAA', 'CAG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'I': ['AUU', 'AUC', 'AUA'],
    'M': ['AUG'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'N': ['AAU', 'AAC'],
    'K': ['AAA', 'AAG'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'D': ['GAU', 'GAC'],
    'E': ['GAA', 'GAG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
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

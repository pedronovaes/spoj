# After identifying the exons (segment used in translation) and introns (not
# used in translation) of an RNA string, we only need to delete the introns and
# concatenate the exons to form a new string ready for translation.
import re
import sys
from rna import dna_to_rna
from prot import rna_to_protein


def generate_protein(dna, introns):
    """
    Generates a protein from DNA.

    Keyword arguments:
    dna -- DNA chain
    introns -- list of nucleotides who are not used in translation
    """
    for i in introns:
        dna = dna.replace(i, '')

    rna = dna_to_rna(dna)
    prot = rna_to_protein(rna)

    return prot


if __name__ == '__main__':
    FASTA = ''.join(sys.stdin.read().split('\n'))
    FASTA = re.split(pattern='>Rosalind_[0-9]+', string=FASTA)[1:]

    dna = FASTA[0]
    introns = FASTA[1:]

    prot = generate_protein(dna, introns)
    print(prot)

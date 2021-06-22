import sys
import re
from prot import CODON_TABLE  # I am using the codon table from prot exercise


if __name__ == '__main__':
    prot = re.findall(pattern='.{1,1}', string=sys.stdin.read())

    total_number = 3  # I am starting with 3 because we have 3 STOP codons
    for aminoacid in prot:
        total_number *= len(CODON_TABLE[aminoacid])
    total_number %= 1000000

    print(total_number)

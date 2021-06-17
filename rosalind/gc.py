# In this exercise, I will computing the molecules GC-content, the percentage
# of cytsine and guanine bases in a strand of nucleic acid.
import sys

FASTA = ''.join(sys.stdin.read().split('\n'))

big_gc_content = 0.0

for dna in FASTA.split('>')[1:]:
    id = dna[:13]
    dna = dna[13:]
    gc_content = round((dna.count('G') + dna.count('C')) / len(dna) * 100, 6)

    if gc_content > big_gc_content:
        big_gc_content = gc_content
        assoc_id = id

print(assoc_id)
print(big_gc_content)

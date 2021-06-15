import sys

dna = sys.stdin.read()

# Reversing
dnar = dna[::-1]

# Complement
dnarc = dnar.replace('A', 't') \
    .replace('T', 'a') \
    .replace('C', 'g') \
    .replace('G', 'c') \
    .upper()

print(dnarc)

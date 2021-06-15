import sys

dna = sys.stdin.read()

# For this problem, I am using count method because it is a low level C in
# python, so it is bound to be faster than any loop.
A = dna.count('A')
C = dna.count('C')
G = dna.count('G')
T = dna.count('T')

print(A, C, G, T)

import sys
import math
from itertools import permutations

n = int(sys.stdin.read())

# Generating factorial
print(math.factorial(n))

# Generating permutations with itertools
perm = permutations([*range(1, n + 1)])

for p in perm:
    p = [str(i) for i in list(p)]
    p = ' '.join(p)

    print(p)

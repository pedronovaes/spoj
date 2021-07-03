import sys


def generate_offspring(allele1, allele2, offspring):
    for i in allele1:
        for j in allele2:
            offspring.append(i + j)


def mendelian_inheritance(k, m, n):
    """Return the probability that two randomly selected mating organisms will
    produce an individual possessing a dominant allele.

    k -- number of individuals that are homozygous dominant for a factor
    m -- number of individuals that are heterozygous
    n -- number of individuals that are homozygous recessive
    """
    hod = ['YY'] * k
    he = ['Yy'] * m
    hor = ['yy'] * n

    pop = hod + he + hor

    offspring = []

    for i in range(len(pop)):
        for j in range(len(pop)):
            if i != j:
                generate_offspring(allele1=pop[i], allele2=pop[j], offspring=offspring)

    dominant = 0

    for i in offspring:
        if 'Y' in i:
            dominant += 1

    perc = dominant / len(offspring)

    return round(perc, 5)


if __name__ == '__main__':
    organisms = sys.stdin.read().split(' ')
    perc = mendelian_inheritance(k=int(organisms[0]), m=int(organisms[1]), n=int(organisms[2]))
    print(perc)

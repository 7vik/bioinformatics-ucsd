#       G-C for genome  O(n)
def skew(genome):                       
    skews = [0]
    for nuc in genome:
        if nuc == 'G':
            skews.append(skews[-1]+1)
        elif nuc == 'C':
            skews.append(skews[-1]-1)
        else:
            skews.append(skews[-1])
    return skews

if __name__ == "__main__":
    for c in skew('GAGCCACCGCGATA'):
        print(c, end=' ')
    print()
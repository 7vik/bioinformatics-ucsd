def rev_comp(dna_pattern):
    def reverse(nuc):
        if nuc == 'A':
            return 'T'
        if nuc == 'T':
            return 'A'
        if nuc == 'G':
            return 'C'
        if nuc == 'C':
            return 'G'
    comp = [reverse(l) for l in dna_pattern]
    return comp[::-1]

if __name__ == "__main__":
    # f = open('data3.txt', 'r')
    # i = f.readline()
    print(''.join(rev_comp('GATTACA')))




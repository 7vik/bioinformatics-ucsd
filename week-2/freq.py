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

def hamming(p,q):
    l1 = len(p)
    l2 = len(q)
    assert(l1 == l2)
    errors = 0
    for i in range(l1):
        if p[i] != q[i]:
            errors += 1
    return errors

def freq_words_mismatch(text, k, d):
    kmers = [text[i:i+k] for i in range(len(text) - k + 1)]
    kmers_rev = [rev_comp(k) for k in kmers]
    nhood1 = set([i for kmer in kmers for i in neighbors(kmer, d, set())])
    nhood2 = set([i for kmer in kmers_rev for i in neighbors(kmer, d, set())])
    nhood = nhood1.union(nhood2)
    dic = {z:(approx_pattern_count(text, z, d)+approx_pattern_count(text, rev_comp(z), d)) for z in nhood}
    m = max(dic.values())
    for k in dic:
        if dic[k] == m:
            print(k, end=' ')
    print()
    

def approx_pattern_count(text, pattern, d):
    count = 0
    n1 = neighbors(pattern, d, set())
    n2 = neighbors(rev_comp(pattern), d, set())
    for nb in n1:
        n2.add(nb)
    n = list(n2)
    for i in range(len(text) - len(pattern) + 1):
        p = text[i:i+len(pattern)]
        if hamming(p, pattern) <= d:
            count += 1
    return count

def neighbors(str, d, acc):
    if d == 0:
        return acc
    gen = 'ACGT'
    for i in range(len(str)):
        for g in gen:
            new = [c for c in str]
            new[i] = g
            x = ''.join(new)
            acc.add(x)
    return neighbors(str, d-1, acc)

def pattern_to_number(pattern, accumulator):
    if pattern == '':
        return accumulator
    for i in range(len('ACGT')):
        if pattern[0] == 'ACGT'[i]:
            return pattern_to_number(pattern[1:], ((accumulator * 4) + i))

def number_to_pattern(index, k, acc):
    if index == 0:
        return ('A'*k+acc)[-k:]
    return number_to_pattern(index//4, k, 'ACGT'[index % 4]+acc)

if __name__ == "__main__":
    f = open('data8.txt', 'r')
    t = f.readline().strip()
    # t = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    freq_words_mismatch(t, 7, 3)
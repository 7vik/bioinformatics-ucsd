def neighbors(str, d, acc):
    if d == 0:
        acc.add(str)
        return acc
    gen = 'ACGT'
    for i in range(len(str)):
        for g in gen:
            new = [c for c in str]
            new[i] = g
            x = ''.join(new)
            acc.add(x)
    return neighbors(str, d-1, acc)

def hamming(p,q):
    l1 = len(p)
    l2 = len(q)
    assert(l1 == l2)
    errors = 0
    for i in range(l1):
        if p[i] != q[i]:
            errors += 1
    return errors

def pat_match(pattern, genome, d):
    ls = []
    for i in range(len(genome) - len(pattern) + 1):
        if hamming(genome[i:i+len(pattern)], pattern) <= d:
            ls.append(i)
    return ls

def motif_enum(dna, k, d):
    patterns = set()
    for i in range(len(dna[0]) - k + 1):
        for pp in neighbors(dna[0][i:i+k], d, set()):
            flag = True
            for j in range(len(dna)):
                if len(pat_match(pp, dna[j], d)) == 0:
                    flag = False
            if flag:
                patterns.add(pp)
    return patterns

if __name__ == "__main__":
    f = open('data1.txt', 'r')
    k, d = map(int, f.readline().split())
    dna = []
    while True:
        l = f.readline()
        if not l:
            break
        dna.append(l.strip())
    for item in motif_enum(dna, k, d):
        print(item, end=' ')
    print()
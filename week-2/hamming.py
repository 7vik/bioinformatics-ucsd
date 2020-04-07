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
    for i in range(len(genome)):
        if hamming((genome+('F'*len(pattern)))[i:i+len(pattern)], pattern) <= d:
            ls.append(i)
    return ls

if __name__ == "__main__":
    f = open('data4.txt', 'r')
    p = f.readline().strip('\n')
    g = f.readline().strip('\n')
    d = int(f.readline().strip('\n'))
    print(len(pat_match(p,g,d)))

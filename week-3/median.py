def hamming(p,q):
    l1 = len(p)
    l2 = len(q)
    assert(l1 == l2)
    errors = 0
    for i in range(l1):
        if p[i] != q[i]:
            errors += 1
    return errors

def d(kmer, dnas, k):
    return sum([min([hamming(dna[i:i+k], kmer) for i in range(len(dna) - k + 1)]) for dna in dnas])

def median_string(infile):

    # open infile
    with open(infile, 'r') as file:
        k = int(file.readline().strip())
        dna = file.readlines()
        dna_list = []
        # iterate through each dna gene and collect all kmers
        kmers = set()
        for line in dna:
            l = line.strip()
            dna_list.append(l)
            for i in range(len(l) - k + 1):
                p = l[i : i+k]
                kmers.add(p)
            
            # pattern that minimizes d
            min_dist = float('inf')
            for kmer in kmers:
                if min_dist > d(kmer, dna_list, k):
                    min_dist = d(kmer, dna_list, k)
                    median = kmer
    return median


infile = 'data2.txt'
print(median_string(infile))
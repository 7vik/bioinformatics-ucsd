def probable_kmer(text, k, profile):
    kmers = [text[i : i+k] for i in range(len(text) - k + 1)]
    index = {'A':0, 'C':1, 'G':2, 'T':3}
    max_prob = 0.0
    best = kmers[0]
    for kmer in kmers:
        acc = 1; [acc := acc * profile[index[kmer[x]]][x] for x in range(len(kmer))]
        if max_prob < acc:
            max_prob = acc
            best = kmer
    return best

def score(motifs):
    index = "ACGT"
    score = 0
    p = get_profile(motifs)
    for i in range(len(motifs[0])):
        ppaf = [p[j][i] for j in range(len(index))]
        best = index[ppaf.index(max(ppaf))]
        for j in range(len(motifs)):
            if motifs[j][i] != best:
                score += 1
    return score

def greedy_motif_search(dna, k, t):
    best_motifs = [s[: k] for s in dna]
    for i in range(len(dna[0]) - k + 1):
        motif = dna[0][i : i + k]
        motifs = [motif]
        for i in range(1,t):
            profile = get_profile(motifs)
            motifs.append(probable_kmer(dna[i], k, profile))
        if (score(motifs) < score(best_motifs)):
            best_motifs = motifs
    return best_motifs

def get_profile(motifs):
    index = {'A':0, 'C':1, 'G':2, 'T':3}
    profile = [[0 for _ in range(len(motifs[0]))] for _ in range(4)]
    for motif in motifs:
        for i in range(len(motif)):
            profile[index[motif[i]]][i] += 1
    profile = [[(z+1)/(4+len(motifs)) for z in prof] for prof in profile]
    return profile

if __name__ == "__main__":
    with open('data5.txt', 'r') as f:
        k, t = map(int, f.readline().split())
        dna = [f.readline().strip() for _ in range(t)]
        for item in greedy_motif_search(dna, k, t):
            print(item, end='\n')

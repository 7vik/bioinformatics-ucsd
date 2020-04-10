import random as random
import math

def get_profile(motifs):
    index = {'A':0, 'C':1, 'G':2, 'T':3}
    profile = [[0 for _ in range(len(motifs[0]))] for _ in range(4)]
    for motif in motifs:
        for i in range(len(motif)):
            profile[index[motif[i]]][i] += 1
    profile = [[(z+1)/(4+len(motifs)) for z in prof] for prof in profile]
    return profile

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

def probable_kmer(text, k, profile):
    kmers = [text[i : i+k] for i in range(len(text) - k + 1)]
    index = {'A':0, 'C':1, 'G':2, 'T':3}
    max_prob = 0.0
    for kmer in kmers:
        acc = 1; [acc := acc * profile[index[kmer[x]]][x] for x in range(len(kmer))]
        if max_prob < acc:
            max_prob = acc
            best = kmer
    return best

def get_motifs(profile, dna, k):
    return [probable_kmer(z, k, profile) for z in dna]

def rand_motif_search(dna, k ,t):
    motifs =[]
    for d in dna:
        r = random.randint(0,len(d) - k)
        motifs.append(d[r : r + k])
    best_motifs = motifs
    while True:
        profile = get_profile(motifs)
        motifs = get_motifs(profile, dna, k)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs

if __name__ == "__main__":
    with open('data1.txt', 'r') as f:
        k, t = map(int, f.readline().split())
        dna = [f.readline().strip() for _ in range(t)]
        best_score = math.inf
        for _ in range(1000):
            if (s := score(r := rand_motif_search(dna, k, t))) < best_score:
                best_score = s
                best_motifs = r           
        for elem in best_motifs:
            print(elem)
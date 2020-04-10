import random
import math
import copy

def profile_random_kmer(text, k, profile):
    kmers = [text[i : i+k] for i in range(len(text) - k + 1)]
    probs = []
    index = {'A':0, 'C':1, 'G':2, 'T':3}
    max_prob = 0.0
    for kmer in kmers:
        acc = 1; [acc := acc * profile[index[kmer[x]]][x] for x in range(len(kmer))]
        probs.append(acc)
    probs = [z/sum(probs) for z in probs]
    # print(probs)
    # prob_list = [z for i in range(len(text) - k + 1) for z in ([kmers[i]] * int(probs[i]))]
    # print(prob_list)
    return random.choices(kmers, probs)[0]

def get_profile(motifs):
    index = {'A':0, 'C':1, 'G':2, 'T':3}
    profile = [[0 for _ in range(len(motifs[0]))] for _ in range(4)]
    for motif in motifs:
        # print(motif)
        for i in range(len(motif)):
            # print(motif[i])
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

def gibbs_sampler(dna, k, t, N):
    motifs =[]
    for d in dna:
        r = random.randint(0,len(d) - k)
        motifs.append(d[r : r + k])
    best_motifs = copy.deepcopy(motifs)
    for j in range(1, N + 1):
        i = random.randint(0,t-1)
        # print(motifs[0])
        profile = get_profile(motifs[ : i] + motifs[i+1 : ])
        # print('hah')
        motifs[i] = profile_random_kmer(dna[i], k, profile)
        if score(motifs) < score(best_motifs):
            best_motifs = copy.deepcopy(motifs)
    return best_motifs

if __name__ == "__main__":
    with open('data2.txt', 'r') as f:
        k, t, N = map(int, f.readline().split())
        dna = [f.readline().strip() for _ in range(t)]
        best_score = math.inf
        for _ in range(30):
            if (s := score(r := gibbs_sampler(dna, k, t, N))) < best_score:
                best_score = s
                best_motifs = r           
        for elem in best_motifs:
            print(elem)
            pass
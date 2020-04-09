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

if __name__ == "__main__":
    with open('data3.txt', 'r') as f:
        text = f.readline().strip()
        k = int(f.readline().strip())
        profile = [list(map(float, f.readline().split())) for _ in range(4)]
        print(probable_kmer(text, k, profile))



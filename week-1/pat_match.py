def pat_match(pattern, genome):
    for i in range(len(genome) - len(pattern)):
        if genome[i:i+len(pattern)] == pattern:
            print(i, end=' ')
    print()
    return

if __name__ == "__main__":
    # f = open('cholerae.txt', 'r')
    # # pat = f.readline().strip()
    # pat = 'CTTGATCAT'
    # gen = f.readline().strip()
    # # print(pat)
    # # print(gen)
    pat_match('ATA','GACGATATACGACGATA')
    # pat_match('ATAT', 'GATATATGCATATACTT')

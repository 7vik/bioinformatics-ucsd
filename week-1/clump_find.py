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

def comp_freq(text, k):
    freq_arr = []
    for i in range(4**k):
        freq_arr.append(0)
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        j = pattern_to_number(pattern, 0)
        freq_arr[j] += 1
    return freq_arr

def clump_finding(genome, k, L, t):
    freq_patterns = set()
    clump = [0 for _ in range(4**k)]
    text = genome[0:L]
    freq_arr = comp_freq(text, k)
    for i in range(4**k):
        if freq_arr[i] >= t:
            clump[i] = 1
    for i in range(1,(len(genome)-L+1)):
        FirstPattern = genome[i-1:i+k-1]
        index = pattern_to_number(FirstPattern, 0)
        freq_arr[index] -= 1
        LastPattern = genome[i+L-k : i+L]
        index = pattern_to_number(LastPattern, 0)
        freq_arr[index] = freq_arr[index] + 1
        if freq_arr[index] >= t:
            clump[index] = 1
    for i in range(4**k):
            if clump[i] == 1:
                pat = number_to_pattern(i, k, '')
                freq_patterns.add(pat)
    return freq_patterns

if __name__ == "__main__":
    f = open('E_coli.txt', 'r')
    gen = f.readline().strip()
    print(clump_finding(gen, 9, 500, 3))
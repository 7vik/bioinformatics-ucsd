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
        # print(pattern)
        j = pattern_to_number(pattern, 0)
        freq_arr[j] += 1
    return freq_arr


if __name__ == "__main__":
    f = open('data5.txt', 'r')
    txt = f.readline().strip()
    i = int(f.readline().strip())
    # print(txt)
    # print(i)
    new = comp_freq(txt, i)
    for num in new:
        print(num, end=' ')
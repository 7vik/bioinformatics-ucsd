def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        flag = True
        for j in range(len(Pattern)):
            if Text[i+j] != Pattern[j]:
                flag = False
        if flag:
            count += 1
    return count

def freq_words(text, k):
    freq_patterns = []
    count = []
    for i in range(len(text) - k):
        pattern = text[i:i+k]
        count.append(PatternCount(text, pattern))
    max_count = max(count)
    for i in range(len(text) - k):
        if count[i] == max_count:
            freq_patterns.append(text[i:i+k])
    return set(freq_patterns)

if __name__ == "__main__":
    # f = open("data2.txt", "r")
    # text = f.readline()
    # k = int(f.readline())
    # text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    # k = 4
    print(freq_words('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA', 3))
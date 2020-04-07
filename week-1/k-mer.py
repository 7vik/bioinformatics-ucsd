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

if __name__ == "__main__":
    # f = open("data1.txt", "r")
    # r = f.readline().strip()
    # print(r)
    # p = f.readline().strip()
    # print(p)
    # m = open("aer.txt", "w")
    print(PatternCount('ACTGTACGATGATGTGTGTCAAAG','TGT'))


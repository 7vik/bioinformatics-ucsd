import numpy as np

def skew(genome):                       
    skews = [0]
    for nuc in genome:
        if nuc == 'G':
            skews.append(skews[-1]+1)
        elif nuc == 'C':
            skews.append(skews[-1]-1)
        else:
            skews.append(skews[-1])
    return skews

def skew_min(genome):
    sk = np.array(skew(genome))
    return np.where(sk == sk.min())[0].tolist()

if __name__ == "__main__":
    f = open('data1.txt', 'r')
    t = f.readline()
    print(skew_min(t))
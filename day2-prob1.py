import numpy as np

if __name__ == '__main__':
    sums = []
    for i in range(1, 7):
        for j in range(1, 7):
            sums.append(i + j)
    sums = np.array(sums)
    den = sums.shape[0]
    num = sums[sums <= 9].shape[0]
    print str(num) + '/' + str(den)


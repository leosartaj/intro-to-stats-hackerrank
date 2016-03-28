import math
import collections


def mean(arr, l):
    return sum(arr) / len(arr)


def median(arr, l):
    half = l / 2
    if l % 2:
        return arr[half]
    else:
        return mean(arr[half - 1: half + 1], 2)


def mode(arr):
    counter  = collections.Counter(arr)
    mc = counter.most_common()
    return min(x[0] for x in mc if x[1] == mc[0][1])


def std(arr, m, l):
    return math.sqrt(sum((x - m)**2 for x in arr) / l)


if __name__ == '__main__':
    N = input()
    N = raw_input('')
    arr = sorted(map(float, N.split()))
    l = len(arr)
    m = mean(arr, l)
    print "%.1f" % m
    print "%.1f" % median(arr, l)
    print "%d" % mode(arr)
    print "%.1f" % std(arr, m, l)

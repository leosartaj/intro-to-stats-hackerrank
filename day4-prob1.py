from scipy.stats import norm


if __name__ == '__main__':
    rv = norm(loc=30, scale=4)
    print rv.cdf(40)
    print 1 - rv.cdf(21)
    print rv.cdf(35) - rv.cdf(30)

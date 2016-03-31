from scipy.stats import norm


if __name__ == '__main__':
    rv = norm(loc=20, scale=2)
    print rv.cdf(19.5)
    print rv.cdf(22) - rv.cdf(20)

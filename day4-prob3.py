from scipy.stats import norm


if __name__ == '__main__':
    # Consider n = 49 to be large. The distribution can now be assumed
    # by applying CLT
    print norm.cdf(200, loc=205, scale=15/7.0)

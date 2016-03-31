from scipy.stats import norm


if __name__ == '__main__':
    print norm.cdf(2.5, loc=2.4, scale=2/10.0)


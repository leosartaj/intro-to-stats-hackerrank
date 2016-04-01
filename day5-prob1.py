from scipy.stats import pearsonr, spearmanr


if __name__ == '__main__':
    x = [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]
    y = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]
    print pearsonr(x, y)[0]
    print spearmanr(x, y)[0]

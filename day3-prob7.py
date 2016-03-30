from sympy import S


if __name__ == '__main__':
    num = (S(5) / 1000) * (S(500) / 3500)
    den = S(5 * 500 + 8 * 1000 + 10 * 2000) / (3500 *1000)
    print num / den


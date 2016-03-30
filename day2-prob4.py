from sympy import S, binomial


if __name__ == '__main__':
    ans = (S(4) / 9) * (binomial(7, 2) / binomial(10, 2))
    ans += (S(5) / 9) * ((S(3) * S(7)) / binomial(10, 2))
    print ans

from sympy import S


if __name__ == '__main__':
    ans = S(4) / 7 * S(5) / 9 * S(4) / 8
    ans += S(4) / 7 * S(4) / 9 * S(4) / 8
    ans += S(3) / 7 * S(5) / 9 * S(4) / 8
    print ans

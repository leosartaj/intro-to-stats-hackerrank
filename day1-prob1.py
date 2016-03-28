import sympy as sy


def mean(arr):
    return sum(arr) / len(arr)


def std(arr):
    m = mean(arr)
    return sy.sqrt(sum((x - m)**sy.S(2) for x in arr) / len(arr))


if __name__ == '__main__':
    a = [1, 2, 3]
    n = sy.symbols('n')
    b = [1, 2, 3, n]
    target = std(a)
    curr = std(b)
    print max(sy.solveset(curr - target, n)).evalf()

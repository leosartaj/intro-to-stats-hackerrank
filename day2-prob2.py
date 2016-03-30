if __name__ == '__main__':
    cou = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i != j and (i + j) == 6:
                cou += 1
    print str(cou) + '/' + str(36)

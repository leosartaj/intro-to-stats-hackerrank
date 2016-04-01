from sklearn.linear_model import LinearRegression


if __name__ == '__main__':
    x = [[95], [85], [80], [70], [60]]
    y = [85, 95, 70, 65, 70]
    model = LinearRegression().fit(x, y)
    print model.predict(80)[0]

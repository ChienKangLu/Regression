import matplotlib.pyplot as plt
import numpy as np
import math
import random
import csv


def f(x, alpha, beta):
    y = alpha * math.exp(beta * x) +2
    return y


def data():
    X = []
    Y = []
    for x in np.arange(0, 10, 0.1):
        shake = random.uniform(-1.5, 1.5)
        x_value = x
        y_value = round(f(x, 0.2, 0.4) + shake,3)
        X.append(x_value)
        Y.append(y_value)
    return X, Y


def data_csv(X, Y):
    datacsv = [["X", "Y"]]
    for i in range(0, len(X)):
        datacsv.append([X[i], Y[i]])
    return datacsv


def writeFile(datacsv):
    myFile = open('hw1_data.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(datacsv)

    print("Writing complete")

def draw(X, Y):
    plt.scatter(X, Y, color="black", marker='o', alpha=0.5, linestyle='None', picker=True)


def onpick(event):
    ind = event.ind
    print('onpick3 scatter:', ind)


if __name__ == '__main__':
    random.seed(2000)
    fig = plt.figure()
    fig.canvas.mpl_connect('pick_event', onpick)

    X, Y = data()
    print(len(X), X)
    print(len(Y), Y)
    datacsv = data_csv(X,Y)
    print(datacsv)

    writeFile(datacsv)

    draw(X, Y)
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()

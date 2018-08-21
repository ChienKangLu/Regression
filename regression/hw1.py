import matplotlib.pyplot as plt
import numpy as np
import math
import random
import csv

def mean(data):
    sum = 0
    for i in range(0, len(data)):
        sum += data[i]
    return sum / len(data)

def beta(X,Y,Xmean,Ymean):
    XY = 0
    X2 = 0
    for i in range(0, len(X)):
        XY += (X[i]-Xmean)*(Y[i]-Ymean)
        X2 += math.pow(X[i]-Xmean,2)
    return XY/X2


def alpha(Xmean,Ymean,beta):
    return Ymean-beta*Xmean

def estimatef(alpha,beta,x):
    y = alpha * math.exp(beta * x)
    return y

def estimatedata(alpha,beta):
    X = []
    Y = []
    for x in np.arange(0, 10, 0.1):
        x_value = x
        y_value = estimatef(alpha,beta,x_value)
        X.append(x_value)
        Y.append(y_value)
    return X, Y

def draw(X, Y,color):
    plt.scatter(X, Y, color=color, marker='o', alpha=0.5, linestyle='None', picker=True)


if __name__ == '__main__':
    csvfile = open('hw1_data.csv', newline="\n")
    reader = csv.DictReader(csvfile, delimiter=',')
    X = []
    Y = []
    Y_ = []
    for row in reader:
        # print(row["X"],row["Y"])
        x = float(row["X"])
        y = float(row["Y"])
        y_ = math.log(y)
        # print(x, y, y_)
        X.append(x)
        Y.append(y)
        Y_.append(y_)

    draw(X, Y, "black")

    Xmean = mean(X)
    Y_mean = mean(Y_)

    print("Xmean", Xmean)
    print("Y_mean", Y_mean)

    beta = beta(X,Y_,Xmean,Y_mean)
    alpha = alpha(Xmean,Y_mean,beta)

    print("beta",beta)
    print("alpha",alpha)

    real_alpha = math.pow(math.e,alpha)
    print("real_alpha",real_alpha)

    X, Y = estimatedata(real_alpha,beta)
    draw(X, Y, "red")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()






import numpy as np
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv


def f(x, alpha, beta):
    y = alpha * math.exp(beta * x) +2
    return y


def f2(x,y):
    return x*y +x**2 +y**0.5


def data():
    X = []
    Y = []
    Z = []
    for x in np.arange(0, 10, 0.1):
        shake_y = random.uniform(-1.5, 1.5)
        shake_z = random.uniform(-10, 10)
        x_value = x
        y_value = round(f(x, 0.2, 0.4) + shake_y,3)
        z_value = f2(x_value,y_value) + 3*shake_z
        X.append(x_value)
        Y.append(y_value)
        Z.append(z_value)
    return X, Y, Z


def data_csv(X, Y, Z):
    datacsv = [["X", "Y", "Z"]]
    for i in range(0, len(X)):
        datacsv.append([X[i], Y[i], Z[i]])
    return datacsv


def writeFile(datacsv):
    myFile = open('data.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(datacsv)
    print("Writing complete")

random.seed(2000)
X,Y,Z = data()

datacsv = data_csv(X,Y,Z)
print(datacsv)
writeFile(datacsv)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X, Y,Z, color="black", marker="o", alpha=0.5, linestyle='None', picker=True,s=40)
# plt.savefig("data")
plt.show()

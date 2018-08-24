import numpy as np
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def predict_plane(B):
    x = np.arange(0, 10, 1)
    y = np.arange(0, 13, 1)
    X, Y = np.meshgrid(x,y)
    Z = B[0]+B[1]*X+B[2]*Y
    plt3d = fig.gca(projection='3d')
    plt3d.plot_surface(X,Y,Z,alpha=0, edgecolors='black')

    """
    X = []
    Y = []
    Z = []
    # draw the predict line in 3D
    for x in np.arange(0, 10, 1):
        for y in np.arange(0, 13, 1):
            z = np.array([1,x,y]).transpose().dot(B)
            X.append(x)
            Y.append(y)
            Z.append(z)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(X, Y, Z, color="black", marker="o", alpha=0.5, linestyle='None', picker=True, s=40)
    return X, Y, Z
    """

# read data (X,Y,Z)
csv = np.genfromtxt('data.csv', skip_header=1, delimiter=",")

# put data into numpy array
data = np.array(csv)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:,0], data[:,1], data[:,2], color="red", marker="o", alpha=0.5, linestyle='None', picker=True, s=40)

# Get the X part
X = np.array(data[:, :2])

# Add a column vector to the first column of X ( for each b parameters)
X = np.append(np.ones((X.shape[0], 1)), X, axis=1)

# Get the y part ( which are the scalars we want to predict)
y = np.array(data[:, 2])

# Calculate the B with a math closed form
X_t = X.transpose()
B = np.dot(np.linalg.inv(X_t.dot(X)), X_t).dot(y)
print("B:", B)

# draw the predict line in 3D
predict_plane(B)

plt.show()

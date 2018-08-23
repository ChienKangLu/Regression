import numpy as np
import matplotlib.pyplot as plt
'''
https://www.cnblogs.com/lemonbit/p/7593898.html
https://blog.csdn.net/wangxingfan316/article/details/78759399
'''

x_data = [338., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
y_data = [640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]
adagrad = True

def f(x, y):
    b = x
    w = y
    z = 0
    for n in range(len(x_data)):
        z += (y_data[n] - (b + w * x_data[n])) ** 2
    z /= len(x_data)
    return z


def show_contour():
    """
      draw a contour
    """
    x = np.arange(-200, -100, 1)
    y = np.arange(-5, 5, 0.1)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    plt.contourf(X, Y, Z, 24, alpha=0.5, cmap='jet')
    plt.plot([-188.4], [2.67], 'x', ms=12, markeredgewidth=3, color='orange')
    C = plt.contour(X, Y, Z, 24, colors='black')
    plt.clabel(C, inline=True, fontsize=10)
    plt.xlim(-200, -100)
    plt.ylim(-5, 5)
    plt.xlabel(r'$b$', fontsize=16)
    plt.ylabel(r'$w$', fontsize=16)


if __name__ == "__main__":
    show_contour()
    # ydata = b + w * xdata
    b = -120
    w = -4
    if adagrad:
        lr = 1
    else:
        lr = 0.0000001
    iteration = 100000
    b_history = [b]
    w_history = [w]

    # Adagrad
    if adagrad:
        b_lr = 0.0
        w_lr = 0.0

    for iter in range(iteration):
        w_grad = 0
        b_grad = 0
        for n in range(len(x_data)):
            w_grad += 2 * (y_data[n] - (b + w * x_data[n])) * (-x_data[n])
            b_grad += 2 * (y_data[n] - (b + w * x_data[n])) * (-1)
        if adagrad:
            b_lr += b_grad ** 2
            w_lr += w_grad ** 2

        #  update parameters
        if adagrad:
            w = w - lr/np.sqrt(w_lr) * w_grad
            b = b - lr/np.sqrt(b_lr) * b_grad
        else:
            w = w - lr * w_grad
            b = b - lr * b_grad
        w_history.append(w)
        b_history.append(b)
        print(iter)
    plt.plot(b_history, w_history, 'o-', ms=3, lw=1.5, color='black')
    plt.savefig("gradient" + (" with adagrad" if adagrad else ""))
    plt.show()

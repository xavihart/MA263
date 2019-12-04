import matplotlib.pylab as plt
import numpy as np


def Sigmoid(x):
    return 1.0 / (1.0 + pow(np.e, -x))


def cal(x1, x2):
    y11 = Sigmoid(10 * x1)
    y12 = Sigmoid(10 * x2)
    y13 = Sigmoid(-10 * x1 - 10 * x2 + 300)
    y = Sigmoid(40 * y11 + 40 * y12 + 40 * y13 -100)
    if y  < 0.001:
        return 0
    if y > 0.999:
        return 1
    return y


if __name__ == '__main__':

    g1x = []
    g2x = []
    g3x = []
    g1y = []
    g2y = []
    g3y = []
    for x1 in range(-10, 41):
        for x2 in range(-10, 41):
            y = cal(x1, x2)
            if y == 1:
                g1x.append(x1)
                g1y.append(x2)
            elif y == 0:
                g2x.append(x1)
                g2y.append(x2)
            else:
                g3x.append(x1)
                g3y.append(x2)
    plt.plot(g1x, g1y, 'co', label="y=1", markersize=4)
    plt.plot(g2x, g2y, 'b*', label="y=0", markersize=4)
    plt.plot(g3x, g3y, 'r^', label="y=other", markersize=4)
    plt.legend()
    plt.savefig('./assi10fig.jpg')


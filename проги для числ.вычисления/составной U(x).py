import numpy as np
import matplotlib.pyplot as plt
import math

h = 0.01     #
x0 = -20     #
xn = 20     #
a = 5     #
W_max = 3.5
e = math.e
color = ['r','g','b','c','m','y','k' ]
n = int((xn - x0)/h)
x = [0 for i in range(n + 1)]
x[0] = x0
for i in range(n):
    x[i+1] = x[i] + h


def U(x, a, W_max):
    if -a <= x <= a:
        return 4 - 6/(math.cosh(x))**2
    else:
        return 4 - 6/(math.cosh(x))**2 - (4 - 6/(math.cosh(x))**2 - W_max)*(1 - a**2/x**2)

def search_and_build_grafix(x, a, W_max):
    p = 0
    c = 0
    W_min = -0.2
    W = W_min
    while W < W_max:
        y = [0 for i in range(n + 1)]
        y[0] = e**(math.sqrt(W_max-W)*x[0])
        y[1] = e**(math.sqrt(W_max-W)*x[1])
        y_n = e**(-math.sqrt(W_max-W)*x[n])
        for i in range(1,n):
            y[i + 1] = (2 - h**2*(W - U(x[i],a, W_max))) * y[i] - y[i - 1]
        if abs(y[n]) < 10:
            print(y_n, y[n], W,"v1")
            plt.plot(x, y, label="v1 w^2 = {}".format(round(W,5)), color=color[c], linewidth=2)
            W -= 0.0015
            c += 1
        if y[n] < 0 and p > 0 or y[n] > 0 and p < 0:
             print(y_n, y[n], W, "v2")
             plt.plot(x, y, label="v2 w^2 = {}".format(round(W,5)), color=color[c], linewidth=2)
             W -= 0.0015
             c += 1
        p = y[n]
        W += 0.001
        print(y_n, y[n], W)

    plt.title('График потенциала эта(x) для собственных значений')
    plt.xlabel('x')
    plt.ylabel('эта(x)')
    plt.xlim(-6, 6)
    plt.ylim(-2*a, 2*a)
    plt.grid()  # сетка по отметкам на осях
    plt.legend()  # подписи графиков
    plt.show()

def build_grafix(W,x,a, W_max):
    y = [0 for i in range(n + 1)]
    y[0] = e**(math.sqrt(3.5-W)*x[0])
    y[1] = e**(math.sqrt(3.5-W)*x[1])
    y_n = e**(-math.sqrt(3.5-W)*x[n])
    for i in range(1,n):
        y[i + 1] = (2 - h**2*(W - U(x[i],a, W_max))) * y[i] - y[i - 1]
    print(y_n, y[n], W)
    plt.plot(x, y, label="w^2 = {}".format(round(W*1000)/1000), color='blue', linewidth=2)

    plt.title('График потенциала U(x) для собственных значений')
    plt.xlabel('x')
    plt.ylabel('эта(x)')
    plt.xlim(-6, 6)
    plt.ylim(-2 , 2)
    plt.grid()  # сетка по отметкам на осях
    plt.legend()  # подписи графиков
    plt.show()

def build_U(x, a, W_max):
    c=0
    y = [0 for i in range(n + 1)]
    y[0] = U(x[0],a, W_max)
    y[1] = U(x[1],a, W_max)
    for i in range(1, n):
        y[i + 1] =U(x[i], a, W_max)
    plt.plot(x, y, label='a = {}'.format(a), color=color[c], linewidth=2)
    plt.title('График потенциала U(x)')
    plt.xlabel('x')
    plt.ylabel('эта(x)')
    plt.xlim(-4*a, 4*a)
    plt.ylim(-2.1, 4.2)
    plt.grid()  # сетка по отметкам на осях
    plt.legend()  # подписи графиков
    plt.show()

search_and_build_grafix(x, a, W_max)
# build_grafix(0,x,a, W_max)
# build_U(x, a, W_max)


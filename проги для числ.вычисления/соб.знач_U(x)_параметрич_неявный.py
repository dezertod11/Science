import numpy
import numpy as np
import matplotlib.pyplot as plt
import math

x0 = -10
xn = 10
h = 0.001
W = -1
fi_u = 1-1*10**(-10)
fi_d = -(1-1*10**(-10))
n = int((xn - x0)/h)


def U(fi):
    return 6*fi**2 - 2
def x(fi):
    return math.atanh(fi)

def bin_search(fi_u, fi_d , x_i):
    u = fi_u
    d = fi_d
    # x_r = x(u)
    # x_l = x(d)
    fi_s = (u + d) / 2
    x_s = x(fi_s)
    while abs(x_s - x_i) > 0.01:
        fi_s = (u + d)/2
        x_s = x(fi_s)
        # print(x_s, fi_s )
        if x_s < x_i:
            # x_l = x_s
            d = fi_s
            # print(x_s, fi_s, 1)
        else:
            # x_r = x_s
            u = fi_s
            # print(x_s, fi_s,2)
    return fi_s
def U_data(fi_u, fi_d, x0, xn, h):
    U_array = []
    for x_i in np.arange(x0, xn, h):
        fi_i = bin_search(fi_u, fi_d, x_i)
        U_array.append(U(fi_i))
        if (x_i-x0)/(xn-x0)*100%10 <0.005:
            print("Загрузка потенциала U:",(x_i-x0)/(xn-x0)*100)
    return U_array


U_array = U_data(fi_u, fi_d, x0, xn, h)
# print(U_array)
e = math.e
p = 0
while W < 4:
    y = [0 for i in range(n + 1)]
    y[0] = e**(math.sqrt(4-W)*x0)
    y[1] = e**(math.sqrt(4-W)*(x0+h))
    i = 1
    for xi in np.arange(x0, xn-2*h, h):
        y[i + 1] = (2 - h**2*(W - U_array[i])) * y[i] - y[i - 1]
        i += 1
    # if abs(y[n]) < 1:
    print(y[n-1], W,"v1")
        # plt.plot(np.arange(x0, xn, h), y, label="v1 w^2 = {}".format(W), color='blue', linewidth=2)
        # W += 0.5
    # elif y[n] < 0 and p > 0 or y[n] > 0 and p < 0:
    #      print(y[n], W, "v2")
         # plt.plot(np.arange(x0, xn, h), y, label="v2 w^2 ={}".format(W), color='red', linewidth=2)
         # W += 0.5
    p = y[n]
    W += 0.01






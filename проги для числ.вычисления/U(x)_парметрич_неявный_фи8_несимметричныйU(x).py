import numpy as np
import matplotlib.pyplot as plt
import math
e = math.e

def U(fi):
    return 4*fi**2*(14*fi**4 - 15*fi**2 + 3)
def x(fi):
    return - 1/(math.sqrt(2)*fi) + 1/(math.sqrt(2))*math.atanh(fi)

fi_min = math.sqrt((5 + math.sqrt(11))/14)
fi_max =  math.sqrt((5 - math.sqrt(11))/14)
x0 = x(fi_max)
x_min = x(fi_min)
xn = 11
h = 0.0001
U_min = U(fi_min)
# W = U_min
W = -0.1
fi_u = 1#-1*10**(-50)
fi_d = 0#1*10**(-55)
n = int((xn - x0)/h)
U_max = U(fi_max)


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
        if (x_i-x0)/(xn-x0)*100%10 <0.01:
            print("Загрузка потенциала U:",(x_i-x0)/(xn-x0)*100)
    return U_array


U_array = U_data(fi_u, fi_d, x0, xn, h) #массив U(x)
p = 0
plt.plot(np.arange(x0, xn, h), U_array, label="настоящий", color='blue', linewidth=2)

plt.title('График потенциала U(x)')
plt.xlabel('x')
plt.ylabel('U(x)')
plt.xlim(-5, 7)
plt.ylim(-3, 10)
plt.grid() # сетка по отметкам на осях
plt.legend()  # подписи графиков
plt.show()
while W < U_max:
    y = [0 for i in range(n + 1)]
    y[0] = e**(math.sqrt(U_max - W)*x0)
    y[1] = e**(math.sqrt(U_max - W)*(x0 + h))
    i = 1
    for xi in np.arange(x0, xn-2*h, h):
        y[i + 1] = (2 - h**2*(W - U_array[i])) * y[i] - y[i - 1]
        i += 1
    # if abs(y[n]) < 1:
    print(y[n], W)
        # plt.plot(np.arange(x0, xn, h), y, label="v1 w^2 = {}".format(W), color='blue', linewidth=2)
        # W += 0.5
    # if y[n] < 0 and p > 0 or y[n] > 0 and p < 0:
    if abs(y[n]) < 1100:
         print(y[n], W, "v")
         plt.plot(np.arange(x0, xn, h), y, label="v2 w^2 ={}".format(W), color='red', linewidth=2)
    p = y[n]
    W += 0.001
plt.title('График потенциала U(x)')
plt.xlabel('x')
plt.ylabel('U(x)')
plt.xlim(-5, 5)
plt.ylim(-2, 2)
plt.grid() # сетка по отметкам на осях
plt.legend()  # подписи графиков
plt.show()
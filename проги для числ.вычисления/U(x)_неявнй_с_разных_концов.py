import numpy as np
import matplotlib.pyplot as plt
import math

# Задаем начальные условия
x0 = -3
xn = 3
xk = 2.99 #чиcло xk должно быть недалеко от конца, иначе ничего не получится
h = 0.001
W = -1
fi_u = 1-1*10**(-15)
fi_d = -(1-1*10**(-15))
n = int((xn - x0)/h)
k = int((xk - x0)/h)


def U(fi):
    return 6*fi**2 - 2
def x(fi):
    return math.atanh(fi)

def bin_search(fi_u, fi_d , x_i): #ищем fi_i для каждого x_i
    u = fi_u
    d = fi_d
    # x_r = x(u)
    # x_l = x(d)
    fi_s = (u + d) / 2
    x_s = x(fi_s)
    while abs(x_s - x_i) > 0.001:
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
def U_data(fi_u, fi_d, x0, xn, h): #создаём массив U для точек от x0 до xn
    U_array = []
    for x_i in np.arange(x0, xn, h):
        fi_i = bin_search(fi_u, fi_d, x_i)
        U_array.append(U(fi_i))
        if (x_i-x0)/(xn-x0)*100%10 <0.005:
            print("Загрузка потенциала U:",(x_i-x0)/(xn-x0)*100, "%")
    return U_array


U_array = U_data(fi_u, fi_d, x0, xn, h)
# print(U_array)
e = math.e
p = 0

# Поиск соб. знач
while W < 4:
    # слева направо
    y1 = [0 for i in range(k + 2)]
    y1[0] = e**(math.sqrt(4-W)*x0)
    y1[1] = e**(math.sqrt(4-W)*(x0+h))
    i = 1
    for xi in np.arange(x0, xk, h):
        y1[i + 1] = (2 - h**2*(W - U_array[i])) * y1[i] - y1[i - 1]
        i += 1
    # справа налево
    y2 = [0 for i in range(n - k + 1)]
    y2[n-k] = e ** (math.sqrt(4 - W) * (-xn))
    y2[n-k-1] = e ** (math.sqrt(4 - W) * (-(xn - h)))
    i = n - k - 1
    for xi in np.arange(xk, xn, h):
        y2[i - 1] = (2 - h**2*(W - U_array[i])) * y2[i] - y2[i + 1]
        i -= 1
    Wr = y2[0]*(y1[k+1] - y1[k])/h - y1[k+1]*(y2[1] - y2[0])/h
    # if abs(Wr) < 1:
    #     print(y[n], W,"v1")
    #     plt.plot(np.arange(x0, xn, h), y, label="v1 w^2 = {}".format(W), color='blue', linewidth=2)
    #     W += 0.5
    if Wr < 0 and p > 0 or Wr > 0 and p < 0:
         print(Wr, W, "v2")
         # plt.plot(np.arange(x0, xn, h), y, label="v2 w^2 ={}".format(W), color='red', linewidth=2)
         # W += 0.5
    W += 0.01
    p = Wr
    # print(y2[0]*(y1[k+1] - y1[k])/h - y1[k+1]*(y2[1] - y2[0])/h, W)
    # print((y1[k] - y1[k - 1])/h,(y2[1] - y2[0])/h,W)
plt.plot(np.arange(x0, xn, h), U_array, label="v1 w^2 = {}".format(W), color='blue', linewidth=2)
plt.title('График потенциала U(x) для собственных значений')
plt.xlabel('x')
plt.ylabel('эта(x)')
plt.xlim(-10, 10)
plt.ylim(-3, 5)
plt.grid() # сетка по отметкам на осях
plt.legend()  # подписи графиков
plt.show()
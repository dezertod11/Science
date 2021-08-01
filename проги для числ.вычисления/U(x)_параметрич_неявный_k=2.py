import numpy as np
import matplotlib.pyplot as plt
import math
e = math.e
k = 2
def U(fi):
    return 8*(1 - fi**2)**2*(7*fi**2 - 1)
def x(fi):
    return fi/(2*(1 - fi**2)) + 1/2*math.atanh(fi)

fi_min = 0
U_min = U(fi_min)
W = U_min
# W = -0.1
# fi_max =  math.sqrt(3/7)
# U_max = U(fi_max)

# xl = x(-fi_max)
# xr = x(fi_max)
x0 = -40
xn = 40
h = 0.0005
# fi_u = math.sqrt(3/7)
# fi_d = -fi_u
fi_u = 1
fi_d = -1
n = int((xn - x0)/h)
color = ['r','g','b','c','m','y','k' ]


def bin_search(fi_u, fi_d , x_i):
    u = fi_u
    d = fi_d
    # x_r = x(u)
    # x_l = x(d)
    fi_s = (u + d) / 2
    x_s = x(fi_s)
    while abs(x_s - x_i) > 0.0005:
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
        # if xl < x_i < xr:
        fi_i = bin_search(fi_u, fi_d, x_i)
        U_array.append(U(fi_i))
        # else:
        #     U_array.append(U_max)
        if (x_i-x0)/(xn-x0)*100%10 < h:
            print("Загрузка потенциала U:",round((x_i - x0)/(xn - x0)*100,1),"%")
    return U_array


U_array = U_data(fi_u, fi_d, x0, xn, h) #массив U(x)
plt.plot(np.arange(x0, xn, h), U_array, label="k = 2", color='blue', linewidth=2)#график U(x)
plt.title('График потенциала U(x)')
plt.xlabel('x')
plt.ylabel('U(x)')
plt.xlim(x0 - 20*h, xn + 20*h)
plt.ylim(-10, 10)
plt.grid() # сетка по отметкам на осях
plt.legend()  # подписи графиков
plt.show()
p = 0
c = 0
W = -0.1
U_max = 0
while W < U_max:
    y = [0 for i in np.arange(x0, xn, h)]
    y[0] = e**(math.sqrt(0 - W)*x0)
    y[1] = e**(math.sqrt(0 - W)*(x0 + h))
    i = 1
    for xi in np.arange(x0, xn-2.1*h, h):
        y[i + 1] = (2 - h**2*(W - U_array[i])) * y[i] - y[i - 1]
        i += 1
    print(round(y[n-1],9), round(W, 10))
    if y[n-1] < 0 and p > 0 or y[n-1] > 0 and p < 0:
        plt.plot(np.arange(x0, xn, h), y, label="w^2 = {}".format(round(W,10)), color=color[c%len(color)], linewidth=1.5)
        print(round(y[n-1],9), round(W,10), "victory")
        print(y)
        c += 1
    p = y[n-1]
    W += 0.0001
plt.title('График эта(x)')
plt.xlabel('x')
plt.ylabel('эта(x)')
plt.xlim(x0 - 20*h, xn + 200*h)
plt.ylim(-100, 50)
plt.grid() # сетка по отметкам на осях
plt.legend()  # подписи графиков
plt.show()
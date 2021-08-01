import numpy as np
import matplotlib.pyplot as plt
import math
e = math.e

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
x0 = -5
xn = 5
xk = 3
h = 0.0005
# fi_u = math.sqrt(3/7)
# fi_d = -fi_u
fi_u = 1
fi_d = -1
n = int((xn - x0)/h)
k = int((xk - x0)/h)
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
p = 0

plt.plot(np.arange(x0, xn, h), U_array, label="k = 2", color='blue', linewidth=2)#график U(x)
plt.title('График потенциала U(x)')
plt.xlabel('x')
plt.ylabel('U(x)')
plt.xlim(x0 - 20*h, xn + 20*h)
plt.ylim(-10, 10)
plt.grid() # сетка по отметкам на осях
plt.legend()  # подписи графиков
plt.show()
c = 0
W = -1.583346
U_max = 0
while W < U_max:
    # слева направо
    y1 = [0 for i in range(k + 2)]
    y1[0] = e**(math.sqrt(U_max-W)*x0)
    y1[1] = e**(math.sqrt(U_max-W)*(x0+h))
    i = 1
    for xi in np.arange(x0, xk, h):
        y1[i + 1] = (2 - h**2*(W - U_array[i])) * y1[i] - y1[i - 1]
        i += 1
    # справа налево
    y2 = [0 for i in range(n - k + 1)]
    y2[n-k] = e ** (math.sqrt(U_max-W) * (-xn))
    y2[n-k-1] = e ** (math.sqrt(U_max-W) * (-(xn - h)))
    i = n - k - 1
    for xi in np.arange(xk, xn, h):
        y2[i - 1] = (2 - h**2*(W - U_array[i])) * y2[i] - y2[i + 1]
        i -= 1
    Wr = y2[0]*(y1[k+1] - y1[k])/h - y1[k+1]*(y2[1] - y2[0])/h
    if Wr < 0 and p > 0 or Wr > 0 and p < 0:
         print(Wr, W, "victory")
         plt.plot(np.arange(x0, xk + 1.2*h, h), y1, label="y1 w^2 ={}".format(round(W,6)), color='red', linewidth=2)
         plt.plot(np.arange(xk - 0.5*h, xn, h), y2, label="y2 w^2 ={}".format(round(W,6)), color='blue', linewidth=2)
    W += 0.001
    p = Wr
    print(Wr, W)
plt.title('График эта(x)')
plt.xlabel('x')
plt.ylabel('эта(x)')
plt.xlim(x0 - 20*h, xn + 200*h)
plt.ylim(-100, 50)
plt.grid() # сетка по отметкам на осях
plt.legend()  # подписи графиков
plt.show()
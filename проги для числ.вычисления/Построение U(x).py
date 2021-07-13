import numpy as np
import matplotlib.pyplot as plt
import math

h = 0.001     #
x0 = -100     #
xn = 100     #
n = int((xn - x0)/h)
x = [0 for i in range(n + 1)]
x[0] = x0

for i in range(n):
    x[i+1] = x[i] + h


e = math.e
p = 0
W = -1

def U(x):
    return 4 - 6/(math.cosh(x))**2
while W < 4:
    y = [0 for i in range(n + 1)]
    y[0] = e**(math.sqrt(4-W)*x[0])
    y[1] = e**(math.sqrt(4-W)*x[1])
    y_n = e**(-math.sqrt(4-W)*x[n])


    for i in range(1,n):
        (math.tanh(x[i])) ** 2
        y[i + 1] = (2 - h**2*(W - U(x[i]))) * y[i] - y[i - 1]
    if abs(y[n]) < 1:
        print(y_n, y[n], W,"v1")
        plt.plot(x, y, label="v1 w^2 = {}".format(W), color='blue', linewidth=2)
        W += 0.5
    elif y[n] < 0 and p > 0 or y[n] > 0 and p < 0:
         print(y_n, y[n], W, "v2")
         plt.plot(x, y, label="v2 w^2 ={}".format(W), color='red', linewidth=2)
         W += 0.5
    p = y[n]
    W += 0.001

plt.title('График потенциала U(x) для собственных значений')
plt.xlabel('x')
plt.ylabel('эта(x)')
plt.xlim(-5, 5)
plt.ylim(-1.2, 1.2)
plt.grid() # сетка по отметкам на осях
plt.legend()  # подписи графиков
plt.show()
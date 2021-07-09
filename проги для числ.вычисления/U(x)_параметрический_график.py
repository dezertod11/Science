import numpy
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.misc import derivative

def V(fi):
    return 1/2*(1-fi**2)**2
def d2V(fi):
    return derivative(V,fi,dx=10**(-6),n=2)
fi = np.arange(-0.99999999999999, 1, 1*10**(-6))
x=[]
for i in fi:
    x.append(math.atanh(i))
plt.plot(x, d2V(fi),label="подделка", color='red', linewidth=3)

def U(x):
    U=[]
    for i in np.arange(-5, 5, 0.001):
        U.append(4 - 6/(math.cosh(i))**2)
    return U
plt.plot(np.arange(-5, 5, 0.001), U(1),label="настоящий", color='blue', linewidth=2)

plt.title('График потенциала U(x)')
plt.xlabel('x')
plt.ylabel('U(x)')
plt.xlim(-5, 5)
plt.ylim(-3, 5)
plt.grid() # сетка по отметкам на осях
plt.legend()  # подписи графиков
plt.show()
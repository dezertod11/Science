import numpy as np
import matplotlib.pyplot as plt
import queue as SimpleQueue
import math

quality = 10000001
q = SimpleQueue
x = np.linspace(-1, 1, quality)
f = x*np.cos(2*x)

ff = np.cos(2*x) - 2*x*np.sin(2*x)
gg = []
gg.append(ff[0])
for i in range(1,quality-1):
    gg.append((f[i+1] - f[i-1])/(2*(2/(quality-1))))
gg.append(ff[quality-1])

plt.plot(x, ff, label="настоящая производная", color='red', linewidth=2)
plt.plot(x, gg,  label='численный метод', color='blue', linewidth=2)
plt.show()

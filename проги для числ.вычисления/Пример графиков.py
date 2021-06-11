import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 200)  # отрезок [0, 4π] из 200 точек
yline = 0.04 * x
ysin = np.exp(-x/(2*np.pi))*np.sin(x)  # exp(-x/2π) sin(x)

# добавление графиков
plt.plot(x, ysin, label='затухающее колебание', color='red', linewidth=2)
plt.plot(x, yline, label='прямая', color='blue', linewidth=3)

# название всего графика и подписи к осям
plt.title('Пример построения двух графиков')
plt.xlabel('абсцисса')
plt.ylabel('ордината')

# ограничение видимой области графика
plt.xlim(0, 12)
plt.ylim(-1, 1)

# отметки на абсциссе, первый аргумент - положения, второй - подписи
plt.xticks(np.arange(0, 5*np.pi, np.pi), [ str(i) + 'π' for i in range(6) ])

plt.grid()  # сетка по отметкам на осях
plt.legend()  # подписи графиков

plt.show()
# plt.savefig('temp.png', dpi=90)  # расскомментировать для сохранения картинки
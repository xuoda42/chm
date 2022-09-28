from functools import reduce

import matplotlib.pyplot as plt
import numpy as np
from math import *

class Newton:

    def __init__(self, f, a):
        self.f = f
        if len(a) == 3:
            self.l = a[0]
            self.r = a[1]
            self.step = int(a[2])
        else:
            self.l = 0
            self.r = a[0]
            self.step = int(a[1])
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        # self.ax.set_xlim([self.l - 1, self.r + 1])
        # self.ax.set_ylim([-1.2, 1.2])
        self.ax.set(title='Интерполирование полиномом Ньютона: вперёд')
        self.execute_func()

    def execute_func(self):
        x = np.linspace(self.l, self.r, 1000)
        y = tuple(map(eval(self.f), x))
        self.ax.plot(x, y, label=f'Исходная функция: {self.f}(x)')
        x = np.linspace(self.l, self.r, 5)
        y = tuple(map(eval(self.f), x))
        self.ax.scatter(x, y, color='orange', label='Узлы интерполирования')
        self.newton_pol(x, y)

    def newton_pol(self, x, y):
        N = []
        for i in range(len(x)):
            N.append((y[i] - sum(N[j] * self.multiplier_newton(x, j, None, i) for j in range(i))) / self.multiplier_newton(x, i, None, i))
        xi = np.linspace(self.l, self.r, self.step)
        y = []
        for i in xi:
            y.append(sum(N[k] * self.multiplier_newton(x, k, i) for k in range(len(N))))
        self.ax.plot(tuple(xi), tuple(y), color='indigo', linestyle='-.', label='Полученная интерполяция')
        self.show_graphic()

    def multiplier_newton(self, x, n, xm=None, k=0):
        if n == 0:
            return 1
        if xm == None:
            return reduce(lambda x, y: x * y, [x[k] - x[i] for i in range(n)])
        return reduce(lambda x, y: x * y, [xm - x[i] for i in range(n)])

    def show_graphic(self):
        self.ax.legend()
        plt.show()

def main():
    with open('input.txt') as inf:
        f = inf.readline().strip()
        a = [float(i) for i in inf.readline().strip().split()]
    nawton = Newton(f, a)


if __name__ == '__main__':
    main()
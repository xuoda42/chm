from functools import reduce

import matplotlib.pyplot as plt
import numpy as np
from math import *


def syn_1(x):
    return sin(x ** 2)


def syn_2(x):
    return -(x + 2)**2 * (x - 1)**3 + 5


class Newton:

    def __init__(self, f, a):
        self.f = f
        if len(a) == 4:
            self.l = a[0]
            self.r = a[1]
            self.step = int(a[2])
            self.cnt = int(a[3])
        else:
            self.l = 0
            self.r = a[0]
            self.step = int(a[1])
            self.cnt = int(a[2])
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        # self.ax.set_xlim([self.l - 1, self.r + 1])
        # self.ax.set_ylim([-5, 5])
        self.ax.set(xlabel='Ось абсцисс', ylabel='Ось ординат', title='Интерполирование полиномом Ньютона: Вперёд')
        self.execute_func()

    def execute_func(self):
        x = np.linspace(self.l, self.r, self.step)
        y = tuple(map(eval(self.f), x))
        self.ax.plot(x, y, label=f'Исходная функция: {self.f}(x)')
        x = np.linspace(self.l, self.r, self.cnt)
        y = tuple(map(eval(self.f), x))
        self.ax.scatter(x, y, color='orange', label='Узлы интерполирования')
        self.newton_pol(x, y)

    def newton_pol(self, x, y):
        N = []
        h = x[1] - x[0]
        for i in range(len(x)):
            N.append((y[i] - sum(N[j] * self.multiplier_newton(x, j, None, i) / (pow(h, j) * factorial(j)) for j in range(i))) * pow(h, i) * factorial(i) / self.multiplier_newton(x, i, None, i))
        xi = np.linspace(self.l, self.r, self.step)
        yi = []
        for i in xi:
            yi.append(sum(N[k] * self.multiplier_newton(x, k, i) / (pow(h, k) * factorial(k)) for k in range(len(N))))
        self.ax.plot(tuple(xi), tuple(yi), color='indigo', linestyle='-.', label='Полученная интерполяция')
        # x = np.linspace(self.l, self.r, self.step)
        # y = list(map(eval(self.f), x))
        # x = np.array(x)
        # y = np.array(y)
        # yi = np.array(yi)
        # self.ax.fill_between(x, yi, where=yi!=0, interpolate=True, color='indigo', alpha=0.5)
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
from math import log, sin, cos, exp, tan
import numpy as np
import matplotlib.pyplot as plt

context = {
    'log': log,
    'sin': sin,
    'cos': cos,
    'exp': exp,
    'tan': tan,
}
h = 0.01


def read_file(name_file):
    temp_dict = {}
    with open(name_file) as inf:
        temp_dict['F'] = inf.readline().strip()
        temp_dict['left'] = float(inf.readline().strip())
        temp_dict['right'] = float(inf.readline().strip())
        temp_dict['count_points'] = int(inf.readline().strip())
    return temp_dict


def show_graphic(ax):
    ax[1].legend()
    ax[0].legend()
    plt.show()


def get_value_function(x, func):
    context.update({'x': x})
    return eval(func, context)


def find_points_function(x, data):
    temp_lst = []
    for i in x:
        temp_lst.append(get_value_function(i, data['F']))
    return temp_lst


def get_value_derivative_second_order(x, func):
    context.update({'x': x - h})
    left_val = eval(func, context)
    context.update({'x': x + h})
    right_val = eval(func, context)
    return (-0.5 * left_val + 0.5 * right_val) / h


def find_points_derivative_second_order(x, data):
    temp_lst = []
    for i in range(1, len(x) - 1):
        temp_lst.append(get_value_derivative_second_order(x[i], data['F']))
    return temp_lst


def get_value_derivative_fourth_order(x, func):
    context.update({'x': x - 2 * h})
    left_left_val = eval(func, context)
    context.update({'x': x - h})
    left_val = eval(func, context)
    context.update({'x': x + 2 * h})
    right_right_val = eval(func, context)
    context.update({'x': x + 2 * h})
    right_val = eval(func, context)
    return ((1 / 12) * left_left_val - (2 / 3) * left_val + (2 / 3) * right_val - (1 / 12) * right_right_val) / h


def find_points_derivative_fourth_order(x, data):
    temp_lst = []
    for i in range(3, len(x) - 3):
        temp_lst.append(get_value_derivative_fourth_order(x[i], data['F']))
    return temp_lst


def find_derivative(data):
    fig, ax = plt.subplots(nrows=2, ncols=1)
    ax[0].set(title='Второй порядок точности')
    ax[1].set(title='Четвёртый порядок точности')
    x = np.linspace(data['left'], data['right'], data['count_points'])
    y = find_points_function(x, data)
    ax[0].plot(x, y, label=f'Исходная функция: {data["F"]}')
    ax[1].plot(x, y, label=f'Исходная функция: {data["F"]}')
    y = find_points_derivative_second_order(x, data)
    x = np.linspace(data['left'], data['right'], data['count_points'] - 2)
    ax[0].plot(x, y, label=f'Второй порядок точности')
    y = find_points_derivative_second_order(x, data)
    x = np.linspace(data['left'], data['right'], data['count_points'] - 4)
    ax[1].plot(x, y, label=f'Четвёртый порядок точности', color='green')
    show_graphic(ax)


def main():
    data = read_file('input.txt')
    find_derivative(data)


if __name__ == "__main__":
    main()
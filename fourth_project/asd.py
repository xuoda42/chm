from math import log, sin, cos, exp


h = 0.01
E = 1e-5


def read_file(name_file):
    with open(name_file) as inf:
        n = int(inf.readline().strip())
        dt = []
        for i in range(n):
            dt.append(inf.readline().strip())
    return dt


def find_point(data, start_point={'x': 1, 'y': 5}):
    x_k = eval(data[0], start_point)
    y_k = eval(data[1], {'x': x_k, 'y': start_point['y'], 'log': log, 'cos': cos, 'sin': sin, 'exp': exp})
    try:
        while max(abs(start_point['x'] - x_k), abs(start_point['y'] - y_k)) >= E:
            start_point['x'] = x_k
            start_point['y'] = y_k
            x_k = eval(data[0], start_point)
            y_k = eval(data[1], {'x': x_k, 'y': start_point['y'], 'log': log, 'cos': cos, 'sin': sin, 'exp': exp})
            print('Невязка: ', max(abs(start_point['x'] - x_k), abs(start_point['y'] - y_k)))
    except Exception:
        print(start_point['x'], start_point['y'])
    print(start_point['x'], start_point['y'])


def cx_is(data, start_point):
    h_point_x = start_point.copy()
    h_point_x['x'] += h
    try:
        if (eval(data[0], h_point_x) - eval(data[0], start_point)) / h + \
                (eval(data[1], h_point_x) - eval(data[1], start_point)) / h > 1:
            return False
    except TypeError:
        return False
    h_point_y = start_point.copy()
    h_point_y['y'] += h
    try:
        if (eval(data[0], h_point_y) - eval(data[0], start_point)) / h + \
                (eval(data[1], h_point_y) - eval(data[1], start_point)) / h > 1:
            return False
    except TypeError:
        return False
    return True


def main():
    data = read_file('input.txt')
    with open('start_point.txt') as inf:
        x = float(inf.readline().strip())
        y = float(inf.readline().strip())
        start_point = {
            'x': x,
            'y': y,
        }
        start_point.update(
            {
                'log': log,
                'sin': sin,
                'cos': cos,
                'exp': exp,
            }
        )
    if cx_is(data, start_point):
        find_point(data, start_point)
    else:
        print('Начальная точка не соответствует условиям.')


if __name__ == "asd":
    main()

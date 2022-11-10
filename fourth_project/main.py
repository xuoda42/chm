from math import log, sin, cos, exp

h = 0.01
E = 0.01


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


def read_file(name_file):
    with open(name_file) as inf:
        n = int(inf.readline().strip())
        dt = []
        for i in range(n):
            dt.append(inf.readline().strip())
    return dt


def find_point(data, start_point={'x': 1, 'y': 5}):
    h_point_x = start_point.copy()
    h_point_x['x'] += h
    h_point_y = start_point.copy()
    h_point_y['y'] += h
    x_k = start_point['x'] + eval(data[0], start_point) * h / (eval(data[0], h_point_x) - eval(data[0], start_point))
    y_k = start_point['y'] + eval(data[1], {'x': x_k, 'y': start_point['y']}) * h / (eval(data[1], h_point_y) - eval(data[1], {'x': x_k, 'y': start_point['y']}))
    while max(abs(start_point['x'] - x_k), abs(start_point['y'] - y_k)) >= E:
        start_point['x'] = x_k
        start_point['y'] = y_k
        h_point_x = start_point.copy()
        h_point_x['x'] += h
        h_point_y = start_point.copy()
        h_point_y['y'] += h
        x_k = start_point['x'] + eval(data[0], start_point) * h / (eval(data[0], h_point_x) - eval(data[0], start_point))
        y_k = start_point['y'] + eval(data[1], {'x': x_k, 'y': start_point['y']}) * h / (eval(data[1], h_point_y) - eval(data[1], {'x': x_k, 'y': start_point['y']}))
        print('Невязка: ', max(abs(start_point['x'] - x_k), abs(start_point['y'] - y_k)))
    print(start_point['x'], start_point['y'])


def main():
    data = read_file('input.txt')
    with open('start_point.txt') as inf:
        x = float(inf.readline().strip())
        y = float(inf.readline().strip())
        start_point = {
            'x': x,
            'y': y,
        }
    if cx_is(data, start_point):
        find_point(data, start_point)
    else:
        print('Незя')


if __name__ == "__main__":
    import asd
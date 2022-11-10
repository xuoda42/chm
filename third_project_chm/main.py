import numpy as np

E = 1e-10


def read_file():
    data = {}
    with open('input.txt') as inf:
        data.update(
            {
                'function': inf.readline().strip(),
                'left': float(inf.readline().strip()),
                'right': float(inf.readline().strip()),
                'count_point': int(inf.readline().strip()),
                'count_part': int(inf.readline().strip()),
                'start_point': {}
            }
        )
    return data


def get_y_point(x, func):
    y = []
    for i in x:
        y.append(eval(func, {'x': i}))
    return y


def found_root(data):
    points_rezult = set()
    for x_point in data['start_point'].values():
        fn = eval(data['function'], {'x': x_point})
        while abs(fn) >= E:
            xn = x_point - fn ** 2 / (eval(data['function'], {'x': x_point + fn}) - fn)
            x_point = xn
            fn = eval(data['function'], {'x': x_point})
        flag = True
        for point in points_rezult:
            if abs(point[0] - x_point) < 1e-3:
                flag = False
                break
        if flag:
            points_rezult.add((x_point, fn))
    return points_rezult


def found_start_point(data):
    temp_dict = {'start_point': {}}
    for id_point in range(1, len(data['x'])):
        if ((data['y'][id_point - 1] * data['y'][id_point] <= 0 and data['y'][id_point] and data['y'][id_point - 1])
                or abs(data['y'][id_point]) <= 1e-5):
            id_start_point = len(temp_dict['start_point']) + 1
            temp_dict['start_point'].update({id_start_point: data['x'][id_point]})
        if abs(data['y'][id_point]) <= 1e-5:
            while abs(data['y'][id_point]) <= 1e-5:
                id_point += 1
            id_point += 1
    return temp_dict


def main():
    data = read_file()
    x = np.linspace(data['left'], data['right'], data['count_point'])
    y = get_y_point(x, data['function'])
    data.update(
        {
            'x': x,
            'y': y,
        }
    )
    data.update(found_start_point(data))
    # print(data['start_point'])
    for pair in found_root(data):
        print(pair)


if __name__ == '__main__':
    main()

import collections


class memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value


@memoized
def recursion(number, wires_len, previous_height):
    weight = 1
    if number > 0:
        max_distance = recursion(number - 1, length(weight, previous_height, heighs[number]) + wires_len,
                                 heighs[number])
        min_distance = recursion(number - 1, length(weight, previous_height, 1) + wires_len, 1)
    if number == 0:
        max_distance = (length(weight, previous_height, heighs[number]) + wires_len, heighs[number])
        min_distance = (length(weight, previous_height, 1) + wires_len, 1)
    if min_distance[0] < max_distance[0]:
        wires_len = max_distance[0]
        current_height = max_distance[1]
    else:
        wires_len = min_distance[0]
        current_height = min_distance[1]
    return wires_len, current_height


def length(distance, h1, h2):
    h = max(h1, h2) - min(h1, h2)
    return pow((pow(h, 2) + pow(distance, 2)), 0.5)


def max_dictance():
    return round(max(recursion(len(heighs) - 2, 0, 1)[0],
                     recursion(len(heighs) - 2, 0, heighs[len(heighs) - 1])[0]),
                 2)


if __name__ == '__main__':
    heighs = [100, 2, 100, 2, 100]
    print(max_dictance())

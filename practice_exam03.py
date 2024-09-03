
def walk(stop, start=1):
    print(start, end=" ")
    if start + 1 < stop:
        walk(stop, start + 1)


walk(3)


def process(data):
    data = [1, 2, 3]
    return data[-2]


measurements = [0 for i in range(3)]
process(measurements)
print(measurements[-2])


def combine(width, height=10, depth=0, is_3D=False):
    return [is_3D, width, height, depth]


print(combine(height=1, width=2)[3])

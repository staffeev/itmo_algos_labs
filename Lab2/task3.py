def _make_vector(p1,  p2):
    _x = p2[0] - p1[0]
    _y = p2[1] - p1[1]
    return _x, _y


def o_n_cube(n: int):
    """Пусть есть n точек на координатной плоскости. Сколько существует
    троек точек (p1, p2, p3), что сумма векторов, образованных точками 
    (p1, p2) и (p2, p3) соответственно (где 1-я точка - начало вектора, 2-я - конец)
    является вектором, образующим тупой угол с положительным направлением оси Ox"""

    from math import atan2, degrees
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    count = 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                vec1 = _make_vector(points[x], points[y])
                vec2 = _make_vector(points[y], points[z])
                vec3 = (vec1[0] + vec2[0], vec1[1] + vec2[1])
                if 90 < degrees(atan2(vec3[1], vec3[0])) < 180:
                    count += 1
    return count


if __name__ == "__main__":
    print(o_n_cube(int(input())))
    
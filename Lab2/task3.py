def _make_vector(p1,  p2):
    _x = p2[0] - p1[0]
    _y = p2[1] - p1[1]
    return _x, _y


def o_n_cube() -> int:
    """Пусть есть n точек на координатной плоскости. Сколько существует
    троек точек (p1, p2, p3), что сумма векторов, образованных точками 
    (p1, p2) и (p2, p3) соответственно (где 1-я точка - начало вектора, 2-я - конец)
    является вектором, образующим тупой угол с положительным направлением оси Ox?"""

    n = int(input())
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
                if vec3[0] < 0 and vec3[1] > 0:
                    count += 1
    return count


def o_n_fact() -> int:
    """Сколько существует перестановок длины n таких, что сумма первого и 
    последнего элемента делит сумму оставшихся?"""

    from itertools import permutations
    n = int(input())
    count = 0
    p = list(permutations(range(1, n + 1)))

    s = n * (1 + n) // 2
    for i in p:
        if (s - i[0] - i[-1]) % (i[0] + i[-1]) == 0:
            count += 1
    return count


def o_n_logn() -> int:
    """Пусть бинарное число s задается с помощью массива bounds = [x1, ..., xn], 
    где xi = 1 если xi >= k иначе 0; k - параметр. Найти ближайшее к числу p число, 
    получамое с помощью такого массива"""
    n, p = map(int, input().split())
    bounds = list(map(int, input().split()))
    sorted_bounds = sorted(bounds, reverse=True)
    left, right = 0, n - 1
    min_abs = 10**12
    closest_num = None

    for i in sorted_bounds:
        bin_number = [1 if x >= i else 0 for x in bounds]
        value = int("".join(map(str, bin_number)), 2)
    
    while left <= right:
        mid = (left + right) // 2
        bin_number = [1 if x >= sorted_bounds[mid] else 0 for x in bounds]
        value = int("".join(map(str, bin_number)), 2)
        if (cur_abs := abs(p - value)) < min_abs:
            min_abs = cur_abs
            closest_num = value
        if value <= p:
            left = mid + 1
        else:
            right = mid - 1

    return closest_num


def o_3n() -> int:
    """Дан массив a целых чисел длины n. Какова длина наибольшего общего префикса
    массива префиксных сумм исходного массива и массива префиксных сумм 
    развернутого исходного массива, если префиксы этих двух массивов могут 
    отличаться не более чем в 3 позициях?"""

    n = int(input())
    a = list(map(int, input().split()))
    pref = [0] * n
    pref[0] = a[0]
    for i in range(1, n):
        pref[i] = pref[i - 1] + a[i]
    suf = [0] * n
    suf[0] = a[-1]
    for i in range(1, n):
        suf[i] = suf[i - 1] + a[n - i - 1]
    
    count = 0
    num_of_mistakes = 3
    for i, j in zip(pref, suf):
        if i == j:
            count += 1
        elif num_of_mistakes > 0:
            count += 1
            num_of_mistakes -= 1
        else:
            break

    return count


def _sign(n):
    return 1 if n > 0 else -1 if n < 0 else 0


def _find(s: list[int], n: int):
    left, right = 0, n - 1
    flag = False
    while left  + 1 < right:
        mid = (left + right) // 2
        if _sign(s[left]) != _sign(s[mid]):
            flag = True
            right = mid
        else:
            left = mid
    if not flag:
        return -1
    return min(mid - 1, mid, mid + 1, key=lambda x: abs(s[x]))


def o_3logn() -> int:
    """Пусть даны три дискретные монотонные функции. 
    Найти для каждой такой x, что f(x) наиболее близка к корню функции"""
    n = int(input())
    
    f = list(map(float, input().split()))
    g = list(map(float, input().split()))
    h = list(map(float, input().split()))
    return _find(f, n), _find(g, n), _find(h, n)


if __name__ == "__main__":
    # print(o_n_cube())
    #print(o_n_fact())
    #print(o_n_logn())
    # print(o_3n())
    print(o_3logn())
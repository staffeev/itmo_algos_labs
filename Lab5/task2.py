import simple_colors as sc
from random import randint


def print_min_cost_table(table):
    print()
    print("Количество скалярных операций для вычисления произведения матриц Ai...Aj")
    s = "i\j\t" + "\t".join(map(str, range(1, len(table) + 1)))
    print(sc.green(s))
    for x, i in enumerate(table):
        print(sc.green(str(x + 1)), *i, sep="\t") 
    print()


def get_tree(i: int, j: int, parents: dict):
    """Возвращает бинарное дерево, представляющее порядок умножения матриц"""
    if i == j:
        return i
    return get_tree(i, parents[i, j], parents), get_tree(parents[i, j] + 1, j, parents)


def get_order(tree):
    """Возвращает порядок умножения матриц"""
    if isinstance(tree, int):
        return f"A{tree + 1}"
    return f"({get_order(tree[0])}) * ({get_order(tree[1])})"


def find_min_cost(sizes: list[int], print_table_flag=False):
    """Нахождение минимального числа операций для умножения матриц"""
    n = len(sizes) - 1
    min_cost = [[0 for _ in range(n)] for _ in range(n)]
    parents = {}

    for i_j in range(1, n):
        for i in range(n - i_j):
            j = i + i_j
            min_cost[i][j] = 10**12
            for k in range(i, j):
                num_of_operations = sizes[i] * sizes[k + 1] * sizes[j + 1] 
                value = min_cost[i][k] + min_cost[k + 1][j] + num_of_operations
                if value < min_cost[i][j]:
                    min_cost[i][j] = value
                    parents[i, j] = k
    
    if print_table_flag:
        print_min_cost_table(min_cost)
    
    return min_cost[0][n - 1], get_tree(0, n - 1, parents)


def multiply_matrices(m1, m2) -> list[list[int]]:
    """Умножение двух матриц"""
    n, m, k = len(m1), len(m1[0]), len(m2[1])
    m3 = [[0 for _ in range(k)] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            m3[i][j] = sum(m1[i][p] * m2[p][j] for p in range(m))
    return m3


def multiply_tree(tree) -> list[list[int]]:
    """Умножает матрицы в нужном порядке"""
    if isinstance(tree, int):
        return matrices[tree]
    return multiply_matrices(multiply_tree(tree[0]), multiply_tree(tree[1]))


def create_matrices(n: int, lb: int, rb: int, k: int):
    """Создание случайных матриц"""
    sizes = [randint(lb, rb) for _ in range(n + 1)]
    matrices = []
    for i in range(1, n + 1):
        matrix = [[randint(-k, k) for _ in range(sizes[i])] for _ in range(sizes[i - 1])]
        matrices.append(matrix)
    return sizes, matrices


if __name__ == "__main__":
    sizes, matrices = create_matrices(n=10, lb=3, rb=7, k=5)
    print("Массив размеров:", sc.cyan(sizes))
    n = len(sizes) - 1
    # умножение подряд
    res = multiply_matrices(matrices[0], matrices[1])
    for i in range(2, n):
        res = multiply_matrices(res, matrices[i])
    print(sc.yellow("Результат умножения матриц:"))
    for i in res:
        print(i)
    print("Количество операций при умножении матриц подряд:", sc.red(sum(sizes[i - 1] * sizes[i] * sizes[i + 1] for i in range(1, n))))
    print()
    # умножение в оптимальноя порядке
    num_of_operations, tree = find_min_cost(sizes, print_table_flag=True)
    print(sc.yellow("Результат множения матриц в оптимальном порядке (такой же):"))
    res = multiply_tree(tree)
    for i in res:
        print(i)
    print("Количество операций при умножении в оптимальном порядке:", sc.green(num_of_operations))
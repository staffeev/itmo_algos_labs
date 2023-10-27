import simple_colors as sc
from collections import deque

EMPTY_BLOCK = sc.cyan("0")
PATH_BLOCK = sc.red("x")


class Board:
    """Класс поля. Нужен для прикольной отрисовки"""
    def __init__(self, n, m):
        self.width, self.height = m, n
        self.field = []  # 0, 1 и x
    
    def set_field(self):
        self.field = [list(map(int, input().split())) for _ in range(n)]
    
    def set_path(self, points: list[tuple[int]]):
        for point in points:
            self.field[point[0]][point[1]] = "x"

    def __repr__(self):
        """Вывод с раскрашиванием"""
        return "\n".join([" ".join([
            EMPTY_BLOCK if x == 0 else PATH_BLOCK if x == "x" else str(x) for x in i
        ]) for i in self.field])
    
    def __str__(self):
        return repr(self)


def check_in_borders(x, y, n, m):
    """Проверяет, что координаты точки находятся в пределах поля"""
    return 0 <= x <= n - 1 and 0 <= y <= m - 1


def get_neighbours(x, y, n, m):
    """Возвращает соседние точки для (x, y), которые принадлежат полю"""
    neighbours = [(x + i, y + j) for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
    return [i for i in neighbours if check_in_borders(i[0], i[1], n, m)]


def bfs(start: tuple[int], n: int, m: int, field: list[list[int]]):
    """Поиск в глубину. Находит ближайший выход из лабиринта"""
    queue = deque([start])
    end = None
    parents = {}
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]] = 1

    while queue:
        (x0, y0) = queue.popleft()
        if (x0 in (0, n - 1) or y0 in (0, m - 1)) and not visited[x0][y0]:
            end = (x0, y0)
            break
        visited[x0][y0] = 1

        for (x, y) in get_neighbours(x0, y0, n, m):
            if not visited[x][y] and field[x][y] == 0:
                parents[x, y] = (x0, y0)
                queue.append((x, y))
    
    if end is None:  # Выхода не оказалось
        return []
    
    # Получение пути
    path = []
    while end != start:
        path.append(end)
        end = parents[end]
    path.append(end)
    return path[::-1]


if __name__ == "__main__":
    n, m = map(int, input("Введите размер массива: ").split())
    board = Board(n, m)
    board.set_field()
    start = tuple(map(int, input("Введите координаты стартовой точки: ").split()))
    board.set_path(bfs(start, n, m, board.field))
    print(board)

from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import deque
import numpy as np

# Настройка холста
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.invert_zaxis()
ax.invert_yaxis()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.zaxis.set_major_locator(MaxNLocator(integer=True))


class Board:
    """Класс поля"""
    def __init__(self, n, m, k):
        self.width, self.height, self.count = m, n, k
        self.field = []  # 0, 1 и x
    
    def set_field(self):
        for _ in range(self.count):
            self.field.append([list(map(int, input().split())) for _ in range(self.height)])
            print()
    
    def set_path(self, points: list[tuple[int]]):
        for point in points:
            self.field[point[0]][point[1]][point[2]] = "x"
    

    def visualize(self):
        coords = [[], [], []]
        walls = [[], [], []]
        colors = []
        for p in range(self.count):
            for i in range(self.width):
                for j in range(self.height):
                    if self.field[p][i][j] != 1:
                        coords[0].append(j)
                        coords[1].append(i)
                        coords[2].append(p)
                        colors.append({"0": "cyan", "x": "red"}[str(self.field[p][i][j])])
                    else:
                        walls[0].append(j)
                        walls[1].append(i)
                        walls[2].append(p)
        
        ax.scatter(*coords, c=colors, alpha=1)
        ax.scatter(*walls, c="gray", alpha=0.05)
        plt.show()


def check_in_borders(x, y, z, n, m, k):
    """Проверяет, что координаты точки находятся в пределах поля"""
    return 0 <= x <= n - 1 and 0 <= y <= m - 1 and 0 <= z <= k - 1


def get_neighbours(x, y, z, n, m, k):
    """Возвращает соседние точки для (x, y), которые принадлежат полю"""
    shifts = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0),  (0, 0, -1), (0, 0, 1)]
    neighbours = [(x + i, y + j, z + p) for i, j, p in shifts]
    return [i for i in neighbours if check_in_borders(*i, n, m, k)]


def bfs(start: tuple[int], n: int, m: int, k: int, field: list[list[list[int]]]):
    """Поиск в глубину. Находит ближайший выход из лабиринта"""
    queue = deque([start])
    end = None
    parents = {}
    visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(k)]
    visited[start[0]][start[1]][start[2]] = 1

    while queue:
        (z0, x0, y0) = queue.popleft()
        if (x0 in (0, n - 1) or y0 in (0, m - 1) or z0 in (0, k - 1)) and not visited[z0][x0][y0]:
            end = (z0, x0, y0)
            break
        visited[z0][x0][y0] = 1

        for (x, y, z) in get_neighbours(x0, y0, z0, n, m, k):
            if not visited[z][x][y] and field[z][x][y] == 0:
                parents[z, x, y] = (z0, x0, y0)
                queue.append((z, x, y))
    
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
    n, m, k = map(int, input("Введите размер массива: ").split())
    board = Board(n, m, k)
    board.set_field()
    start = tuple(map(int, input("Введите координаты стартовой точки: ").split()))
    board.set_path(bfs(start, n, m, k, board.field))
    board.visualize()
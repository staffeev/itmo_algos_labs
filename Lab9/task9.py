import networkx as nx
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")


def find_shortest_path(start_vertex: int, end_vertex: int, num_of_vertexes: int, 
                       num_of_edges: int, g: dict[int, list[dict]]) -> list[int]:
    """Реализация алгоритма Фора-Беллмана"""
    distances = [float("inf")] * (num_of_vertexes + 1)
    distances[start_vertex] = 0
    parents = dict()
    for _ in range(num_of_edges):
        for u in g:
            if distances[u] == float("inf"):
                continue
            for v, w in g[u].items():
                if distances[v] > distances[u] + w:
                    distances[v] = distances[u] + w
                    parents[v] = u
    # проверка на путь отрицательной длины
    for u in g:
        for v, w in g[u].items():
            if distances[u] != float("inf") and distances[v] > distances[u] + w:
                raise ValueError("Cycle with negative length found")
    path = []
    cur_vertex = end_vertex
    while cur_vertex != start_vertex:
        path.append(cur_vertex)
        cur_vertex = parents[cur_vertex]
    path.append(start_vertex)
    return distances[end_vertex], path[::-1]


def create_graph_from_input(directed=False) -> dict[int, list[dict]]:
    """Ввод графа поьзователем"""
    g = dict()
    vertexes = set()
    m = int(input("Введите количество ребер: "))
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u] = g.get(u, {}) | {v: w}
        if not directed:
            g[v] = g.get(v, {}) | {u: w}
        vertexes.add(u)
        vertexes.add(v)
    return len(vertexes), m, g


def convert_graph_to_nx_form(g: dict) -> dict:
    """Преобразование списка ребер к нужному виду"""
    g2 = dict()
    for u in g:
        for v, w in g[u].items():
            g2[u] = g2.get(u, {}) | {v: {"weight": w}}
    return g2


def draw_nx_graph(g: dict, edges_to_colorize: list=[], directed=False):
    """Рисование графа"""
    graph = nx.from_dict_of_dicts(convert_graph_to_nx_form(g), create_using=nx.Graph if not directed else nx.DiGraph)
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, [i for i in graph.edges if i not in edges_to_colorize])
    nx.draw_networkx_edges(graph, pos, edges_to_colorize, edge_color="red")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, "weight"))
    plt.show()



if __name__ == "__main__":
    # Неорграф
    # n, m, g = 9, 6, {1: {2: 7, 3: 9, 6: 14}, 2: {1: 7, 3: 10, 4: 15}, 3: {1: 9, 2: 10, 6: 2, 4: 11}, 6: {1: 14, 3: 2, 5: 9}, 4: {2: 15, 3: 11, 5: 6}, 5: {6: 9, 4: 6}}
    # path_len, path = find_shortest_path(1, 5, n, m, g)
    # print(f"Длина кратчайшего пути равна {path_len}. Путь:", "->".join(map(str, path)))
    # draw_nx_graph(g , [(path[i - 1], path[i]) for i in range(1, len(path))])

    # Орграф
    # n, m, g = 6, 9, {2: {1: 1, 5: 7, 4: 2}, 1: {3: 4}, 3: {2: -2, 4: 3}, 4: {5: 4}, 5: {6: 7}, 6: {4: -3}}
    # path_len, path = find_shortest_path(1, 6, n, m, g)
    # print(f"Длина кратчайшего пути равна {path_len}. Путь:", "->".join(map(str, path)))
    # draw_nx_graph(g , [(path[i - 1], path[i]) for i in range(1, len(path))], True)

    # Цикл отрицательной длины
    n, m, g = 6, 9, {2: {1: 1, 3: -2, 5: 7, 4: 2}, 1: {2: 1, 3: 4}, 3: {1: 4, 2: -2, 4: 3}, 5: {2: 7, 4: 4, 6: 7}, 4: {2: 2, 3: 3, 5: 4, 6: -3}, 6: {5: 7, 4: -3}}
    try:
        path_len, path = find_shortest_path(1, 6, n, m, g)
        print(f"Длина кратчайшего пути равна {path_len}. Путь:", "->".join(map(str, path)))
        draw_nx_graph(g , [(path[i - 1], path[i]) for i in range(1, len(path))])
    except ValueError:
        print("В графе обнаружен цикл отрицательной длины")
        draw_nx_graph(g)
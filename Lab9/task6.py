import networkx as nx
from matplotlib import pyplot as plt


def find_spanning_tree(g: list[tuple]) -> list[tuple]:
    """Реализация алгоритма Крускала"""
    nodes = set()
    edges = []
    ng = dict()
    for (u, v, w) in sorted(g, key=lambda x: x[2]):
        if u in nodes and v in nodes: # проверка на цикл
            continue
        if u not in nodes and v not in nodes:
            ng[u] = ng[v] = [u, v]
        else:
            if not ng.get(u):
                ng[v].append(u)
                ng[u] = ng[v]
            else:
                ng[u].append(v)
                ng[v] = ng[u]

        edges.append((u, v, w))
        nodes.add(u)
        nodes.add(v)

    for (u, v, w) in sorted(g, key=lambda x: x[2]): # объединение групп вершин
        if v not in ng[u]:
            edges.append((u, v, w))
            gr1 = ng[u]
            ng[u] += ng[v]
            ng[v] += gr1  
    
    return edges


def draw_nx_graph(g: list[tuple], edges_to_colorize: list=[]):
    """Рисование графа"""
    graph = nx.Graph()
    graph.add_weighted_edges_from(g)
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, [i for i in graph.edges if i not in edges_to_colorize])
    nx.draw_networkx_edges(graph, pos, edges_to_colorize, edge_color="red")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, "weight"))
    plt.show()


def create_graph_from_input() -> list[dict]:
    """Создание графа пользователем"""
    g = []
    m = int(input("Введите количество ребер: "))
    for _ in range(m):
        u, v, w = map(int, input().split())
        g.append((u, v, w))
    return g


if __name__ == "__main__":
    g = [(1, 2, 7), (1, 4, 5), (2, 4, 9), (2, 3, 8), (2, 5, 7), (3, 5, 5), (4, 5, 15), (4, 6, 6), (5, 6, 8), (5, 7, 9), (6, 7, 11)]
    G = nx.Graph()
    spanning_tree = find_spanning_tree(g)
    edges = [(i[0], i[1]) for i in spanning_tree]
    weight = sum(i[2] for i in spanning_tree)
    print(f"Минимальное остовное дерево имеет вес {weight} и состоит из ребер", edges)
    draw_nx_graph(g, edges)
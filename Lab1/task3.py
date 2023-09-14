from task2 import get_questions_and_answers, create_tree
import networkx as nx
from matplotlib import pyplot as plt


def hierarchy_tree_pos(g: nx.DiGraph, root: str, width: int = 100, pos: dict = {}, 
                       xcenter=0, ycenter=0, ydist=0.1, n_iter=0, rows_to_not_expand=[],
                       expand_value=3.5):
    """Рекурсивная функция, которая располагает узлы дерева так, чтобы получилась
    иерархическая структура"""
    pos[root] = (xcenter, ycenter)
    neigh = list(g.neighbors(root))
    if len(neigh) != 0:
        k = expand_value if n_iter not in rows_to_not_expand else 10**9
        dx = width / (max(1, len(neigh) - n_iter // k))
        nextx = xcenter - width/(max(1, 2 - n_iter // k)) - dx/2
        for node in neigh:
            nextx += dx
            pos = hierarchy_tree_pos(g, node, dx, pos, nextx, ycenter - ydist, 
                                     ydist, n_iter + 1, rows_to_not_expand, expand_value)
    return pos


def format_q(q: str, row_len=15) -> str:
    """Переносит текст по строкам, чтобы длина каждой строки была не больше row_len"""
    if len(q) <= row_len:
        return q
    new_q = ""
    c = 0
    for i in q.split():
        if c + len(i) + 1 <= row_len:
            new_q += i + " "
            c += len(i) + 1
        else:
            new_q += "\n" + i + " "
            c = 0
    return new_q


def create_graph(qnumber: int, prev: str, tree: tuple):
    """Создает граф для отображения"""
    if qnumber == len(fields):
        return
    for i in (1, 0):
        v = prev + str(i)
        g.add_node(v)
        g.add_edge(prev, v, width=3)
        edge_labels[(prev, v)] = "Да" if i == 1 else "Нет"
        new_tree = tree[i]
        if isinstance(new_tree, str):
            new_tree = "\n".join(new_tree.split())
            label_dict[v] = new_tree
        else:
            label_dict[v] = format_q(fields[qnumber])
            create_graph(qnumber + 1, v, new_tree)


if __name__ == "__main__":
    fields, answers = get_questions_and_answers("opros.csv")
    tree = create_tree(0, answers)
    g = nx.DiGraph()
    label_dict = {"": fields[0]}
    edge_labels = {}
    g.add_node("")
    create_graph(1, "", tree)
    plt.figure(figsize=(12, 5))

    pos = hierarchy_tree_pos(g, "", rows_to_not_expand=[4])
    nx.draw(g, pos=pos, labels=label_dict, with_labels=True, font_size=4, node_color="white", width=0.5,
            arrowsize=5, node_size=1000)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=4)
    plt.savefig("Lab1/graph.pdf")
    # plt.show()
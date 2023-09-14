from task2 import get_questions_and_answers
import networkx as nx
from matplotlib import pyplot as plt


def hierarchy_tree_pos(g: nx.DiGraph, root: str, width: int = 100, pos: dict = {}, 
                       xcenter=0, ycenter=0, ydist=0.01, n_iter=0):
    pos[root] = (xcenter, ycenter)
    neigh = list(g.neighbors(root))
    if len(neigh) != 0:
        k = 1000000000000000000
        dx = width / (len(neigh) - n_iter // k)
        nextx = xcenter - width/(2 - n_iter // k) - dx/2
        for node in neigh:
            nextx += dx
            pos = hierarchy_tree_pos(g, node, dx, pos, nextx, ycenter-ydist, ydist,n_iter + 1)
    return pos


def format_q(q: str, row_len=15) -> str:
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


def find_person(v: str) -> int:
    name = None
    c = 0
    for i, j in people.items():
        if j.startswith(v):
            c += 1
            name = i
    return c, name


def create_graph(qnumber: int, prev: str):
    if qnumber == len(fields):
        return
    for i in (1, 0):
        v = prev + str(i)
        g.add_node(v)
        g.add_edge(prev, v, width=3)
        edge_labels[(prev, v)] = "Да" if i == 1 else "Нет"
        c, name = find_person(v)
        if c > 1:
            label_dict[v] = format_q(fields[qnumber])
            create_graph(qnumber + 1, v)
        elif c == 1:
            label_dict[v] = format_q(f"Вы - \n{name}")
        else:
            label_dict[v] = "Такого человека нет!"


if __name__ == "__main__":
    fields, answers = get_questions_and_answers("opros.csv")
    people = {i.person: str(i) for i in answers}
    g = nx.DiGraph()
    label_dict = {"": fields[0]}
    edge_labels = {}
    g.add_node("")
    create_graph(1, "")

    pos = hierarchy_tree_pos(g, "", width=3)
    nx.draw(g, pos=pos, labels=label_dict, with_labels=True, font_size=5, node_color="white", width=0.5,
            arrowsize=5, node_size=500)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=5)
    plt.show()
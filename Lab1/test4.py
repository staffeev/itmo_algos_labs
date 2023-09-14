from task2 import get_questions_and_answers
import networkx as nx
from matplotlib import pyplot as plt
# from networkx.drawing.nx_agraph import graphviz_layout
import random


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    if not nx.is_tree(G):
        raise TypeError(
            'cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            # allows back compatibility with nx version 1.11
            root = next(iter(nx.topological_sort(G)))
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width/len(children)
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc-vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


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
        g.add_edge(prev, v, width=3,length=10)
        edge_labels[(prev, v)] = "Да" if i == 1 else "Нет"
        c, name = find_person(v)
        if c > 1:
            label_dict[v] = fields[qnumber]
            create_graph(qnumber + 1, v)
        elif c == 1:
            label_dict[v] = f"Вы - {name}"
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
    pos = hierarchy_pos(g, "", width=5, vert_gap=0.005)
    # pos = graphviz_layout(g, prog="dot")
    nx.draw(g, pos=pos, labels=label_dict, with_labels=True, font_size=5, node_color="white", width=0.5,
            arrowsize=5)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=3)
    plt.show()
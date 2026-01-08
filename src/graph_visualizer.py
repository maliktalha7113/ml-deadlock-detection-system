import networkx as nx
import matplotlib.pyplot as plt

def draw_wait_for_graph(graph):
    G = nx.DiGraph()

    for p, waits_for in graph.items():
        for q in waits_for:
            G.add_edge(f"P{p}", f"P{q}")

    plt.figure(figsize=(6, 4))
    nx.draw(G, with_labels=True, node_size=2000, node_color="lightblue")
    plt.title("Wait-For Graph")
    plt.show()

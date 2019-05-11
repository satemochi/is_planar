from matplotlib import pyplot as plt
import networkx as nx


def mps_approx(g):
    """
    An approximation algorithm for the maximum planar subgraph problem

    The approximation ratio is 1/3.
    Because algorithm puts at least n-1 edges, while any planar graph
    has at most 3n-6 edges, where n is the number of vertices.

    Parameters
    ----------
    g : networkx.Graph
        a simple undirected graph

    Returns
    -------
    t : networkx.Graph
        a planar subgraph of g

    References
    ----------
    .. [1] C. Buchheim, M. Chimani, C. Gutwenger, M. Jünger, P. Mutzel. (2014)
           "Crossings and planarization",
           Handbook of Graph Drawing and Visualization.
           http://cs.brown.edu/people/rtamassi/gdhandbook/
    """

    t = nx.minimum_spanning_tree(g)
    unprocessed = [e for e in g.edges() if not t.has_edge(*e)]
    for x, y in unprocessed:
        t.add_edge(x, y)
        if not is_planar(t):
            t.remove_edge(x, y)
    return t


if __name__ == '__main__':
    g = nx.petersen_graph()
    p = mps_approx(g)

    pos = nx.spring_layout(g)
    nx.draw_networkx_edges(g, pos, alpha=0.5)
    nx.draw_networkx_edges(p, pos, edge_color='orange', width=2)
    nx.draw_networkx_nodes(g, pos, node_size=100)

    plt.gca().axis('off')
    plt.tight_layout()
    plt.savefig('mps_approx_1.png', bbox_inches='tight')
    plt.show()

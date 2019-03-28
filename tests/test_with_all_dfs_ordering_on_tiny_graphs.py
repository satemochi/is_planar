from itertools import permutations
import unittest
import networkx as nx
from is_planar import is_planar


class TestPlanarity(unittest.TestCase):
    def test_bull(self):
        expected = True
        g = nx.bull_graph()
        for o in enumerate_dfs_ordering_naively(g):
            @spec_order(o)
            def func(g):
                return is_planar(g)
            actual = func(g)
            self.assertEqual(expected, actual)

    def test_house(self):
        expected = True
        g = nx.house_graph()
        for o in enumerate_dfs_ordering_naively(g):
            @spec_order(o)
            def func(g):
                return is_planar(g)
            actual = func(g)
            self.assertEqual(expected, actual)

    def test_cubical(self):
        expected = True
        g = nx.cubical_graph()
        for o in enumerate_dfs_ordering_naively(g):
            @spec_order(o)
            def func(g):
                return is_planar(g)
            actual = func(g)
            self.assertEqual(expected, actual)

    def test_octahedral(self):
        expected = True
        g = nx.octahedral_graph()
        for o in enumerate_dfs_ordering_naively(g):
            @spec_order(o)
            def func(g):
                return is_planar(g)
            actual = func(g)
            self.assertEqual(expected, actual)

    def test_sedgewick(self):
        expected = True
        g = nx.sedgewick_maze_graph()
        for o in enumerate_dfs_ordering_naively(g):
            @spec_order(o)
            def func(g):
                return is_planar(g)
            actual = func(g)
            self.assertEqual(expected, actual)

    def test_petersen(self):
        expected = False
        g = nx.petersen_graph()
        for o in enumerate_dfs_ordering_naively(g):
            @spec_order(o)
            def func(g):
                return is_planar(g)
            actual = func(g)
            self.assertEqual(expected, actual)


def enumerate_dfs_ordering_naively(g):
    for o in permutations(g.nodes(), g.order()):
        if is_dfs_ordering(g, o):
            yield o


def is_dfs_ordering(graph, ordering):
    n = len(ordering)
    for i in xrange(1, n-1):
        sub_ordering = ordering[:i]
        x = greatest_incident_index(graph, sub_ordering, ordering[i])
        y = max(greatest_incident_index(graph, sub_ordering, ordering[j])
                for j in xrange(i+1, n))
        if x < y:
            return False
    return True


def spec_order(order):
    def _spec_order(func):
        def wrapper(*args, **kwargs):
            g = get_ordered_graph(args[0], order)
            res = func(g, **kwargs)
            return res
        return wrapper
    return _spec_order


def get_ordered_graph(g, order):
    og = nx.OrderedGraph()
    og.add_nodes_from(order)
    for i in xrange(1, len(order)):
        v = order[i]
        u = order[greatest_incident_index(g, order[:i], v)]
        og.add_edge(u, v)
    og.add_edges_from(e for e in g.edges() if not og.has_edge(*e))
    return og


def greatest_incident_index(g, sub_ordering, v):
    return max(i if u in g[v] else -1 for i, u in enumerate(sub_ordering))


if __name__ == '__main__':
    unittest.main()

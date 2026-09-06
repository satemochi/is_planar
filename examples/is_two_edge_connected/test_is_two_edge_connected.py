from unittest import TestCase, main
import networkx as nx
from is_two_edge_connected import is_two_edge_connected


class test_two_edge_connectivity(TestCase):
    def test_barbell_graph(self):
        g = nx.barbell_graph(4, 2)
        self.assertTrue(is_two_edge_connected(g) == False)

    def test_complete_graph(self):
        g = nx.complete_graph(4)
        self.assertTrue(is_two_edge_connected(g) == True)

    def test_cycle_graph(self):
        g = nx.cycle_graph(8)
        self.assertTrue(is_two_edge_connected(g) == True)

    def test_empty_graph(self):
        g = nx.empty_graph(8)
        self.assertTrue(is_two_edge_connected(g) == False)

    def test_rary_tree(self):
        g = nx.full_rary_tree(3, 16)
        self.assertTrue(is_two_edge_connected(g) == False)

    def test_path_graph(self):
        g = nx.path_graph(16)
        self.assertTrue(is_two_edge_connected(g) == False)

    def test_lollipop_graph(self):
        g = nx.lollipop_graph(8, 8)
        self.assertTrue(is_two_edge_connected(g) == False)

    def test_petersen_graph(self):
        g = nx.petersen_graph()
        self.assertTrue(is_two_edge_connected(g) == True)

    def test_frucht_graph(self):
        g = nx.frucht_graph()
        self.assertTrue(is_two_edge_connected(g) == True)

    def test_null_graph(self):
        g = nx.null_graph()
        self.assertTrue(is_two_edge_connected(g) == False)


if __name__ == '__main__':
    main()

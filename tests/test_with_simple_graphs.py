import os.path
import pickle
import sys
import unittest
import networkx as nx
from is_planar import is_planar


class TestPlanarity(unittest.TestCase):
    """ In this test, we use files 'graph?*c.g6' can be fetched from
            https://users.cecs.anu.edu.au/~bdm/data/graphs.html

        Each pickle file is made by bit_setter.py on 64-bit 4-core machine.
    """

    def test_six(self):
        graph_data, cheat_sheet = 'g/graph6c.g6', 'g/planar_conn.6.pkl'
        self.__framework(graph_data, cheat_sheet)

    def test_seven(self):
        graph_data, cheat_sheet = 'g/graph7c.g6', 'g/planar_conn.7.pkl'
        self.__framework(graph_data, cheat_sheet)

    def test_eight(self):
        graph_data, cheat_sheet = 'g/graph8c.g6', 'g/planar_conn.8.pkl'
        self.__framework(graph_data, cheat_sheet)

    def test_nine(self):
        graph_data, cheat_sheet = 'g/graph9c.g6', 'g/planar_conn.9.pkl'
        self.__framework(graph_data, cheat_sheet)

    @unittest.skip('too much elapsed time')
    def test_ten(self):
        graph_data, cheat_sheet = 'g/graph10c.g6', 'g/planar_conn.10.pkl'
        self.__framework(graph_data, cheat_sheet)

    def __framework(self, graph_data, cheat_sheet):
        if os.path.isfile(graph_data) and os.path.isfile(cheat_sheet):
            with open(graph_data, 'rb') as f:
                sg = f.read().splitlines()
            with open(cheat_sheet, 'rb') as f:
                bit_vector = pickle.load(f)
            for i, g in enumerate(sg):
                expected = True
                if self.__bit_getter(bit_vector, i) == 0:
                    expected = False
                nx_g = nx.from_graph6_bytes(g)
                actual = is_planar(nx_g)
                if expected != actual:
                    nx.write_gml(nx_g, 'sg.gml')
                nx_g.clear()
                self.assertEqual(expected, actual)

    def __bit_getter(self, bits, idx, word_size=63):
        return 1 & (bits[idx // word_size] >> (idx % word_size))


if __name__ == '__main__':
    unittest.main()

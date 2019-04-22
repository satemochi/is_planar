import mmap
import os.path
import re
import unittest
import networkx as nx
import pynauty
from is_planar import is_planar


class TestPlanarity(unittest.TestCase):
    """ In this test, we use files 'planar_conn.?*.g6' can be fetched from
            https://users.cecs.anu.edu.au/~bdm/data/graphs.html
    """
    def test_six(self):
        sfile, pfile = 'graph6c.g6', 'planar_conn.6.g6'
        self.__framework(sfile, pfile)

    def test_seven(self):
        sfile, pfile = 'graph7c.g6', 'planar_conn.7.g6'
        self.__framework(sfile, pfile)

    def test_eight(self):
        sfile, pfile = 'graph8c.g6', 'planar_conn.8.g6'
        self.__framework(sfile, pfile)

    def test_nine(self):
        sfile, pfile = 'graph9c.g6', 'planar_conn.9.g6'
        self.__framework(sfile, pfile)

    @unittest.skip('too much elapsed time')
    def test_ten(self):
        sfile, pfile = 'graph10c.g6', 'planar_conn.10.g6'
        self.__framework(sfile, pfile)

    def __framework(self, sfile, pfile):
        if os.path.isfile(sfile) and os.path.isfile(pfile):
            with open(sfile) as f:
                sg = f.read().splitlines()
            with open(pfile) as f:
                clp = [self.__cl(g) for g in f.read().splitlines()]
            for g in sg:
                expected = True
                if self.__cl(g) not in clp:
                    expected = False
                actual = is_planar(nx.from_graph6_bytes(g))
                if expected != actual:
                    nx.write_gml(nx.from_graph6_bytes(g), 'sg.gml')
                    print expected, actual
                self.assertEqual(expected, actual)

    def __cl(self, g6):
        """ compute the canonical labeling? from graph6 """
        g = nx.from_graph6_bytes(g6)
        pg = pynauty.Graph(g.order(),
                           adjacency_dict={v: list(g[v]) for v in g})
        return pynauty.certificate(pg)


if __name__ == '__main__':
    unittest.main()

import mmap
import os.path
import re
import unittest
import networkx as nx
from is_planar import is_planar


class TestPlanarity(unittest.TestCase):
    """ In this test, we use files 'planar_conn.?*.g6' can be fetched from
            https://users.cecs.anu.edu.au/~bdm/data/graphs.html
    """
    def test_three(self):
        fname = 'planar_conn.3.g6'
        if os.path.isfile(fname):
            expected = True
            with open(fname) as f:
                for g in f:
                    actual = is_planar(nx.from_graph6_bytes(g.rstrip('\n')))
                    self.assertEqual(expected, actual)

    def test_four(self):
        fname = 'planar_conn.4.g6'
        if os.path.isfile(fname):
            expected = True
            with open(fname) as f:
                for g in f:
                    actual = is_planar(nx.from_graph6_bytes(g.rstrip('\n')))
                    self.assertEqual(expected, actual)

    def test_five(self):
        fname = 'planar_conn.5.g6'
        if os.path.isfile(fname):
            expected = True
            with open(fname) as f:
                for g in f:
                    actual = is_planar(nx.from_graph6_bytes(g.rstrip('\n')))
                    self.assertEqual(expected, actual)

    def test_six(self):
        fname = 'planar_conn.6.g6'
        if os.path.isfile(fname):
            expected = True
            with open(fname) as f:
                for g in f:
                    actual = is_planar(nx.from_graph6_bytes(g.rstrip('\n')))
                    self.assertEqual(expected, actual)

    def test_seven(self):
        fname = 'planar_conn.7.g6'
        if os.path.isfile(fname):
            expected = True
            with open(fname) as f:
                for g in f:
                    actual = is_planar(nx.from_graph6_bytes(g.rstrip('\n')))
                    self.assertEqual(expected, actual)

    def test_eight(self):
        fname = 'planar_conn.8.g6'
        if os.path.isfile(fname):
            expected = True
            with open(fname) as f:
                for g in f:
                    actual = is_planar(nx.from_graph6_bytes(g.rstrip('\n')))
                    self.assertEqual(expected, actual)

    def test_nine(self):
        fname = 'planar_conn.9.g6'
        if os.path.isfile(fname):
            expected = True
            with open(fname, 'r+b') as f:
                mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                sep = re.finditer('(.*)\n', mm)
                for g in sep:
                    actual = is_planar(nx.from_graph6_bytes(g.group(1)))
                    self.assertEqual(expected, actual)

    @unittest.skip('too much elapsed time')
    def test_ten(self):
        fname = 'planar_conn.10.g6'
        if os.path.isfile(fname):
            expected = True
            with open(fname) as f:
                mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                for g in iter(mm.readline, b''):
                    actual = is_planar(nx.from_graph6_bytes(g.rstrip('\n')))
                    self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

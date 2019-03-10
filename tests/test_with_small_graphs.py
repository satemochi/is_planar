from itertools import combinations, product
import random
import unittest
import networkx as nx
from networkx.algorithms.planarity import check_planarity
from is_planar import is_planar


class TestPlanarity(unittest.TestCase):
    def test_balanced_tree(self):
        expected = True
        actual = is_planar(nx.balanced_tree(4, 4))
        self.assertEqual(expected, actual)

    def test_barbells(self):
        expected = True
        actual = is_planar(nx.barbell_graph(4, 4))
        self.assertEqual(expected, actual)
        expected = False 
        actual = is_planar(nx.barbell_graph(5, 2))
        self.assertEqual(expected, actual)
        actual = is_planar(nx.barbell_graph(55, 11))
        self.assertEqual(expected, actual)

    def test_circular_ladder(self):
        expected = True
        actual = is_planar(nx.circular_ladder_graph(15))
        self.assertEqual(expected, actual)

    def test_cycle(self):
        expected = True
        actual = is_planar(nx.cycle_graph(15))
        self.assertEqual(expected, actual)

    def test_dorogovtsev(self):
        """ (reference) Pseudofractal Scale-free Web: planar """
        expected = True
        actual = is_planar(nx.dorogovtsev_goltsev_mendes_graph(7))
        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = True
        actual = is_planar(nx.empty_graph())
        self.assertEqual(expected, actual)
        actual = is_planar(nx.empty_graph(15))
        self.assertEqual(expected, actual)

    def test_ladder(self):
        expected = True
        actual = is_planar(nx.ladder_graph(5))
        self.assertEqual(expected, actual)

    def test_lollipop(self):
        expected = False
        actual = is_planar(nx.lollipop_graph(5, 3))
        self.assertEqual(expected, actual)
        expected = True
        actual = is_planar(nx.lollipop_graph(4, 33))
        self.assertEqual(expected, actual)

    def test_null(self):
        expected = True
        actual = is_planar(nx.null_graph())
        self.assertEqual(expected, actual)

    def test_path(self):
        expected = True
        actual = is_planar(nx.path_graph(100))
        self.assertEqual(expected, actual)

    def test_star(self):
        expected = True
        actual = is_planar(nx.star_graph(100))
        self.assertEqual(expected, actual)

    def test_trivial(self):
        expected = True
        actual = is_planar(nx.trivial_graph())
        self.assertEqual(expected, actual)

    def test_wheel(self):
        expected = True
        actual = is_planar(nx.wheel_graph(100))
        self.assertEqual(expected, actual)

    def test_bull(self):
        expected = True
        actual = is_planar(nx.bull_graph())
        self.assertEqual(expected, actual)

    def test_chvatal(self):
        expected = False
        actual = is_planar(nx.chvatal_graph())
        self.assertEqual(expected, actual)

    def test_cubical(self):
        expected = True
        actual = is_planar(nx.cubical_graph())
        self.assertEqual(expected, actual)

    def test_desargues(self):
        expected = False
        actual = is_planar(nx.desargues_graph())
        self.assertEqual(expected, actual)

    def test_diamond(self):
        expected = True
        actual = is_planar(nx.diamond_graph())
        self.assertEqual(expected, actual)

    def test_dodecahedral(self):
        expected = True
        actual = is_planar(nx.dodecahedral_graph())
        self.assertEqual(expected, actual)

    def test_frucht(self):
        expected = True
        actual = is_planar(nx.frucht_graph())
        self.assertEqual(expected, actual)

    def test_heawood(self):
        expected = False
        actual = is_planar(nx.heawood_graph())
        self.assertEqual(expected, actual)

    def test_house(self):
        expected = True
        actual = is_planar(nx.house_x_graph())
        self.assertEqual(expected, actual)

    def test_house_x(self):
        expected = True
        actual = is_planar(nx.house_x_graph())
        self.assertEqual(expected, actual)

    def test_icosahedral(self):
        expected = True
        actual = is_planar(nx.icosahedral_graph())
        self.assertEqual(expected, actual)

    def test_krackhardt(self):
        expected = True
        actual = is_planar(nx.krackhardt_kite_graph())
        self.assertEqual(expected, actual)

    def test_moebius(self):
        expected = False
        actual = is_planar(nx.moebius_kantor_graph())
        self.assertEqual(expected, actual)

    def test_octahedral(self):
        expected = True
        actual = is_planar(nx.octahedral_graph())
        self.assertEqual(expected, actual)

    def test_pappus(self):
        expected = False
        actual = is_planar(nx.pappus_graph())
        self.assertEqual(expected, actual)

    def test_petersen(self):
        expected = False
        actual = is_planar(nx.petersen_graph())
        self.assertEqual(expected, actual)

    def test_sedgewick(self):
        expected = True
        actual = is_planar(nx.sedgewick_maze_graph())
        self.assertEqual(expected, actual)

    def test_tetrahedral(self):
        expected = True
        actual = is_planar(nx.tetrahedral_graph())
        self.assertEqual(expected, actual)

    def test_truncated_cube(self):
        expected = True
        actual = is_planar(nx.truncated_cube_graph())
        self.assertEqual(expected, actual)

    def test_truncated_tetrahedron(self):
        expected = True
        actual = is_planar(nx.truncated_tetrahedron_graph())
        self.assertEqual(expected, actual)

    def test_tutte(self):
        expected = True
        actual = is_planar(nx.tutte_graph())
        self.assertEqual(expected, actual)

    def test_utility(self):
        expected = False
        actual = is_planar(nx.LCF_graph(6, [3, -3], 3))
        self.assertEqual(expected, actual)

    def test_franklin(self):
        """ 12-vertex cubic graph: non-planar but hamiltonian """
        expected = False
        actual = is_planar(nx.LCF_graph(12, [5, -5], 6))
        self.assertEqual(expected, actual)
        actual = is_planar(nx.LCF_graph(12, [-5, -3, 3, 5], 3))
        self.assertEqual(expected, actual)

    def test_mcgee(self):
        """ 24-vertex 7-cage graph: non-planar """
        expected = False
        actual = is_planar(nx.LCF_graph(24, [-12, 7, -7], 8))
        self.assertEqual(expected, actual)

    def test_levi(self):
        """ 30-vertex incidence graph: non-planar """
        expected = False
        actual = is_planar(nx.LCF_graph(30, [-13, -9, 7, -7, 9, 13], 5))
        self.assertEqual(expected, actual)

    def test_dyck(self):
        expected = False
        actual = is_planar(nx.LCF_graph(32, [-13, 5, -5, 13], 8))
        self.assertEqual(expected, actual)

    def test_gray(self):
        expected = False
        actual = is_planar(nx.LCF_graph(54, [-25, 7, -7, 13, -13, 25], 9))
        self.assertEqual(expected, actual)

    def test_balaban_10(self):
        expected = False
        actual = is_planar(nx.LCF_graph(70, [68,-25,-18,29,13,35,-13,-29,19,25,9,-29,29,17,33,21,9,-13,-31,-9,25,17,9,-31,27,-9,17,-19,-29,27,-17,-9,-29,33,-25,25,-21,17,-17,29,35,-29,17,-17,21,-25,25,-33,29,9,17,-27,29,19,-17,9,-27,31,-9,-17,-25,9,31,13,-9,-21,-33,-17,-29,29], 1))
        self.assertEqual(expected, actual)

    def test_balaban_11(self):
        expected = False
        actual = is_planar(nx.LCF_graph(112, [44,26,-47,-15,35,-39,11,-27,38,-37,43,14,28,51,-29,-16,41,-11,-26,15,22,-51,-35,36,52,-14,-33,-26,-46,52,26,16,43,33,-15,17,-53,23,-42,-35,-28,30,-22,45,-44,16,-38,-16,50,-55,20,28,-17,-43,47,34,-26,-41,11,-36,-23,-16,41,17,-51,26,-33,47,17,-11,-20,-30,21,29,36,-43,-52,10,39,-28,-17,-52,51,26,37,-17,10,-10,-45,-34,17,-26,27,-21,46,53,-10,29,-50,35,15,-47,-29,-41,26,33,55,-17,42,-26,-36,16], 1))
        self.assertEqual(expected, actual)

    def test_foster(self):
        expected = False
        actual = is_planar(nx.LCF_graph(90, [17, -9, 37, -37, 9, -17], 15))
        self.assertEqual(expected, actual)

    def test_biggs_smith(self):
        expected = False
        actual = is_planar(nx.LCF_graph(102, [16,24,-38,17,34,48,-19,41,-35,47,-20,34,-36,21,14,48,-16,-36,-43,28,-17,21,29,-43,46,-24,28,-38,-14,-50,-45,21,8,27,-21,20,-37,39,-34,-44,-8,38,-21,25,15,-34,18,-28,-41,36,8,-29,-21,-48,-28,-20,-47,14,-8,-15,-27,38,24,-48,-18,25,38,31,-25,24,-46,-14,28,11,21,35,-39,43,36,-38,14,50,43,36,-11,-36,-24,45,8,19,-25,38,20,-24,-14,-21,-8,44,-31,-38,-28,37], 1))
        self.assertEqual(expected, actual)

    def test_tutte_12_cage(self):
        expected = False
        actual = is_planar(nx.LCF_graph(126, [17,27,-13,-59,-35,35,-11,13,-53,53,-27,21,57,11,-21,-57,59,-17], 7))
        self.assertEqual(expected, actual)

    def test_bidiakis_cube(self):
        expected = True
        actual = is_planar(nx.LCF_graph(12, [6,4,-4], 4))
        self.assertEqual(expected, actual)

    def test_naruru(self):
        expected = False
        actual = is_planar(nx.LCF_graph(24, [5,-9,7,-7,9,-5], 4))
        self.assertEqual(expected, actual)

    def test_f26a(self):
        expected = False
        actual = is_planar(nx.LCF_graph(26, [-7,7], 13))
        self.assertEqual(expected, actual)

    def test_tutte_coxeter(self):
        expected = False
        actual = is_planar(nx.LCF_graph(26, [-13,-9,7,-7,9,13], 5))
        self.assertEqual(expected, actual)

    def test_harries(self):
        expected = False
        actual = is_planar(nx.LCF_graph(70, [-29,-19,-13,13,21,-27,27,33,-13,13,19,-21,-33,29], 5))
        self.assertEqual(expected, actual)

    def test_harries_wong(self):
        expected = False
        actual = is_planar(nx.LCF_graph(70, [9,25,31,-17,17,33,9,-29,-15,-9,9,25,-25,29,17,-9,9,-27,35,-9,9,-17,21,27,-29,-9,-25,13,19,-9,-33,-17,19,-31,27,11,-25,29,-33,13,-13,21,-29,-21,25,9,-11,-19,29,9,-27,-19,-13,-35,-9,9,17,25,-9,9,27,-27,-21,15,-9,29,-29,33,-9,-25], 1))
        self.assertEqual(expected, actual)

    def test_Ljubljana(self):
        expected = False
        actual = is_planar(nx.LCF_graph(26, [47,-23,-31,39,25,-21,-31,-41,25,15,29,-41,-19,15,-49,33,39,-35,-21,17,-33,49,41,31,-15,-29,41,31,-15,-25,21,31,-51,-25,23,9,-17,51,35,-29,21,-51,-39,33,-9,-51,51,-47,-33,19,51,-21,29,21,-31,-39], 2))
        self.assertEqual(expected, actual)

    def test_goldner_harary(self):
        """ from hagberg test_planarity_networkx.py """
        e = [(1,2), (1,3), (1,4), (1,5), (1,7), (1,8), (1,10),
             (1,11), (2,3), (2,4), (2,6), (2,7), (2,9), (2,10),
             (2,11), (3,4), (4,5), (4,6), (4,7), (5,7), (6,7),
             (7,8), (7,9), (7,10), (8,10), (9,10), (10,11)]
        expected = True
        actual = is_planar(nx.Graph(e))
        self.assertEqual(expected, actual)

    def test_is_planar_unions(self):
        """ from @hagberg test_planarity_networkx.py """
        planar = [nx.path_graph(5), nx.complete_graph(4)]
        non_planar = [nx.complete_graph(5), nx.complete_bipartite_graph(3,3)]
        for g in planar:
            self.assertEqual(True, is_planar(g))
        for g in non_planar:
            self.assertEqual(False, is_planar(g))
        expected = True
        for (g1, g2) in combinations(planar, 2):
            g = nx.disjoint_union(g1, g2)
            self.assertEqual(expected, is_planar(g))
        expected = False
        for (g1, g2) in combinations(non_planar, 2):
            g = nx.disjoint_union(g1, g2)
            self.assertEqual(expected, is_planar(g))
        for (g1, g2) in product(planar, non_planar):
            g = nx.disjoint_union(g1, g2)
            self.assertEqual(expected, is_planar(g))

#    def test_random_planar(self):
#        expected = True
#        for i in xrange(10):
#            for g in random_planar(20, seed=None):
#                actual = is_planar(g)
#                self.assertEqual(expected, actual)

#    def test_vs_check_planarity(self):
#        n = 500
#        for i in xrange(100):
#            g = nx.fast_gnp_random_graph(n, 5./n)
#            expected, _ = check_planarity(g)
#            actual = is_planar(g)
#            if expected != actual:
#                nx.write_gml(g, 'g.gml')
#            self.assertEqual(expected, actual)


def random_planar(n=100, trials=300, seed=0):
    """ A random graph generator based on Markov chain:
        (Ref.) A. Denise, M. Vasconcellos, D. J. A. Welsh, (1996).
                "The Random Planar Graph", Congressus Numerantium.
    """
    random.seed(seed)
    g = nx.empty_graph(n)
    for i in xrange(trials):
        f = random.sample(xrange(n), 2)
        if g.has_edge(*f):
            g.remove_edge(*f)
            yield g
        else:
            g.add_edge(*f)
            is_planar, _ = check_planarity(g)
            if not is_planar:
                g.remove_edge(*f)
            else:
                yield g


if __name__ == '__main__':
    unittest.main()

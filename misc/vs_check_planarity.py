import time
import networkx as nx
from matplotlib import pyplot as plt
from networkx.algorithms.planarity import check_planarity
import sys
sys.path.append('../src')
from is_planar import is_planar


def vs_check_planarity(trials=100):
    N = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
         200, 300, 400, 500, 600, 700, 800, 900, 1000]
#    N = [10, 50, 100, 500, 1000, 1500, 5000, 10000, 50000, 100000]
    ch_p, is_p = [], []
    for n in N:
        print(n)
        cp, ip = 0, 0
        p = 0
        for i in range(trials):
            g = nx.fast_gnp_random_graph(n, 5./n)

            s = time.time()
            actual = is_planar(g)
            e = time.time()
            expected, _ = check_planarity(g)
            cp += time.time() - e
            ip += e - s

            if expected != actual:
                nx.write_gml(g, 'g.gml')
                print(expected, actual)
            if expected:
                p += 1
            g.clear()
        ch_p.append(float(cp) / trials)
        is_p.append(float(ip) / trials)
#        print float(p) / trials
    plt.plot(N, ch_p, label='check_planarity', marker='o')
    plt.plot(N, is_p, label='is_planar', marker='o')
    plt.legend(loc='best')
    plt.xscale('log')
    plt.tight_layout()
#    plt.savefig('vs_check_planarity_1.png', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    vs_check_planarity()

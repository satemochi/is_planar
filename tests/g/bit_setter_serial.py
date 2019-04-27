import os.path
import pickle
import sys
import networkx as nx
import pynauty
from tqdm import tqdm


def cl(g6):
    """ compute the canonical labeling? from graph6 """
    g = nx.from_graph6_bytes(g6)
    adj = {v: list(g[v]) for v in g}
    nauty_graph = pynauty.Graph(g.order(), adjacency_dict=adj)
    s =  pynauty.certificate(nauty_graph)
    g.clear()
    del nauty_graph
    return s


def bit_setter(sg, clp, word_size=63):
    bits = []
    for i, g in enumerate(tqdm(sg)):
        if i % word_size == 0:
            bits.append(0)
        if cl(g) in clp:
            bits[-1] |= 1 << (i % word_size)
    return bits


if __name__ == '__main__':
    sfiles = ['graph6c.g6', 'graph7c.g6', 'graph8c.g6', 'graph9c.g6',
              'graph10c.g6']
    pfiles = ['planar_conn.6.g6', 'planar_conn.7.g6', 'planar_conn.8.g6',
              'planar_conn.9.g6', 'planar_conn.10.g6']
    word_size = sys.maxsize.bit_length()
    for s, p in zip(sfiles, pfiles):
        if os.path.isfile(s) and os.path.isfile(p):
            ofile = p[:-2] + 'pkl'
            if os.path.isfile(ofile):
                continue
            with open(s) as f:
                sg = f.read().splitlines()
            with open(p) as f:
                clp = [cl(g) for g in f.read().splitlines()]
            with open(ofile, 'wb') as f:
                pickle.dump(bit_setter(sg, clp, word_size), f)

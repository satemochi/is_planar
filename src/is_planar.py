from collections import defaultdict
from itertools import islice
import networkx as nx
from fringe import fringe


def is_planar(g):
    if g.size() < 9 or g.order() < 5:
        return True
    if g.size() > 3 * g.order() - 6:
        return False
    visited = defaultdict(lambda: False)
    for v in g.nodes():
        if not visited[v]:
            visited[v] = True
            if not lr_algorithm(g, v, visited):
                return False
    return True


def lr_algorithm(g, root, visited):
    fringes = [[]]
    tree_edges = []
    dfs_heights = defaultdict(lambda: 0)
    dfs_stack = [(root, iter(g[root]))]
    while dfs_stack:
        v, children = dfs_stack[-1]
        try:
            w = next(children)
            if visited[w]:  # back edge
                fringes[-1].append(fringe(dfs_heights[w]))
            else:           # tree edge
                visited[w] = True
                fringes.append([])
                tree_edges.append((v, w))
                dfs_heights[w] = dfs_heights[v] + 1
                dfs_stack.append((w, iter(u for u in g[w] if u != v)))
        except StopIteration:
            dfs_stack.pop()
            if len(fringes) > 1:
                _, w = tree_edges.pop()
                m_fringe = merge_fringes(fringes[-1], dfs_heights[w])
                if m_fringe is None:
                    return False
                fringes.pop()
                if m_fringe.fops:
                    fringes[-1].append(m_fringe)
    return True


def merge_fringes(upper_fringes, dfs_height):
    if len(upper_fringes) > 0:
        upper_fringes.sort()
        merged_fringe = upper_fringes[0]
        for f in islice(upper_fringes, 1, len(upper_fringes)):
            if not merged_fringe.merge(f):
                return None
        merged_fringe.prune(dfs_height)
    return merged_fringe

from collections import deque
from itertools import islice


def is_two_edge_connected(g):  # whether g is 2-edge-connected graph?
    if g.order() < 1:
        return False
    dfs_heights, root = {}, next(iter(g))
    dfs_heights[root] = 0
    if __detect_bridge(g, root, dfs_heights):  # if g has a bridge, then False
        return False
    if len(dfs_heights) != g.order():   # not connected graph
        return False
    return True


def __detect_bridge(g, root, dfs_heights):
    fringes, dfs_stack = [[]], [(root, iter(g[root]))]
    while dfs_stack:
        x, children = dfs_stack[-1]
        try:
            y = next(children)
            if y not in dfs_heights:  # tree edge
                dfs_heights[y] = dfs_heights[x] + 1
                fringes.append([])
                dfs_stack.append((y, iter([u for u in g[y] if u != x])))
            else:
                if dfs_heights[x] > dfs_heights[y]:  # back edge
                    fringes[-1].append(fringe(dfs_heights[y]))
        except StopIteration:
            dfs_stack.pop()
            if len(fringes) > 1:
                try:
                    __merge_fringes(fringes, dfs_heights[dfs_stack[-1][0]])
                except Exception:
                    return True
            if len(fringes[-1]) == 0:
                return True
    return False


def __merge_fringes(fringes, dfs_height):
    if (mf := __get_merged_fringe(fringes.pop())) is not None:
        mf.prune(dfs_height)
        if mf.fops:
            fringes[-1].append(mf)


def __get_merged_fringe(upper_fringes):
    if len(upper_fringes) > 0:
        new_fringe = upper_fringes[0]
        for f in islice(upper_fringes, 1, len(upper_fringes)):
            new_fringe.merge(f)
        return new_fringe


class fringe:
    __slots__ = ['fops']

    def __init__(self, dfs_h=None):
        self.fops = deque() if dfs_h is None else deque([fop(dfs_h)])

    def __repr__(self):
        return str(self.L.l_lo)

    @property
    def H(self):
        return self.fops[0]

    @property
    def L(self):
        return self.fops[-1]

    def merge(self, other):
        self.L.c[0][-1] = min(self.L.l_lo, other.L.l_lo)

    def prune(self, dfs_height):
        if self.L.l_lo > dfs_height:
            raise Exception


class fop:  # fringe opposed subset
    __slots__ = ['c']

    def __init__(self, h):
        self.c = [deque([h]), deque()]

    @property
    def left(self):
        return self.c[0]

    @property
    def right(self):
        return self.c[1]

    @property
    def l_lo(self):
        return self.c[0][-1]

    @property
    def l_hi(self):
        return self.c[0][0]

    @property
    def r_lo(self):
        return self.c[1][-1]

    @property
    def r_hi(self):
        return self.c[1][0]

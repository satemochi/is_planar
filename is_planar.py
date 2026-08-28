from collections import deque
from itertools import islice
__all__ = ['is_planar']


def is_planar(g):
    if g.size() < 9 or g.order() < 5:
        return True
    if g.size() > 3 * g.order() - 6:
        return False
    dfs_heights = {}
    for v in g:
        if v not in dfs_heights:
            dfs_heights[v] = 0
            if not __lr_algorithm(g, v, dfs_heights):
                return False
    return True


def __lr_algorithm(g, root, dfs_heights):
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
                    return False
    return True


def __merge_fringes(fringes, dfs_height):
    if (mf := __get_merged_fringe(fringes.pop())) is not None:
        mf.prune(dfs_height)
        if mf.fops:
            fringes[-1].append(mf)


def __get_merged_fringe(upper_fringes):
    if len(upper_fringes) > 0:
        upper_fringes.sort()
        new_fringe = upper_fringes[0]
        for f in islice(upper_fringes, 1, len(upper_fringes)):
            new_fringe.merge(f)
        return new_fringe


class fringe:
    __slots__ = ['fops']

    def __init__(self, dfs_h=None):
        self.fops = deque() if dfs_h is None else deque([fop(dfs_h)])

    def __lt__(self, other):
        if (diff := self.L.l_lo - other.L.l_lo) != 0:
            return diff < 0
        return self.H.l_hi < other.H.l_hi

    @property
    def H(self):
        return self.fops[0]

    @property
    def L(self):
        return self.fops[-1]

    def merge(self, other):
        other.__merge_t_alike_edges()
        self.__merge_t_opposite_edges_into(other)
        if not self.H.right:
            other.__align_duplicates(self.L.l_hi)
        else:
            self.__make_onion_structure(other)
        if other.H.left:
            self.fops.appendleft(other.H)

    def __merge_t_alike_edges(self):
        if self.H.right:
            raise Exception
        for f in islice(self.fops, 1, len(self.fops)):
            if f.right:
                raise Exception
            self.H.left.extend(f.left)
        self.fops = deque([self.fops[0]])

    def __merge_t_opposite_edges_into(self, other):
        while (not self.H.right and self.H.l_hi > other.H.l_lo):
            other.H.right.extend(self.H.left)
            self.fops.popleft()

    def __align_duplicates(self, dfs_h):
        if self.H.l_lo == dfs_h:
            self.H.left.pop()
            self.__swap_side()

    def __swap_side(self):
        if not self.H.left or (self.H.right and self.H.l_lo > self.H.r_lo):
            self.H.c[0], self.H.c[1] = self.H.c[1], self.H.c[0]

    def __make_onion_structure(self, other):
        lo, hi = (0, 1) if self.H.l_hi < self.H.r_hi else (1, 0)
        if other.H.l_lo < self.H.c[lo][0]:
            raise Exception
        elif other.H.l_lo < self.H.c[hi][0]:
            self.H.c[lo].extendleft(reversed(other.H.left))
            self.H.c[hi].extendleft(reversed(other.H.right))
            other.H.left.clear()
            other.H.right.clear()

    def prune(self, dfs_height):
        left_, right_ = self.__lr_condition(dfs_height)
        while self.fops and (left_ or right_):
            if left_:
                self.H.left.popleft()
            if right_:
                self.H.right.popleft()
            if not self.H.left and not self.H.right:
                self.fops.popleft()
            else:
                self.__swap_side()
            if self.fops:
                left_, right_ = self.__lr_condition(dfs_height)

    def __lr_condition(self, dfs_height):
        return (self.H.left and self.H.l_hi >= dfs_height,
                self.H.right and self.H.r_hi >= dfs_height)


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

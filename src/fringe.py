from itertools import islice
from collections import deque
from fringe_opposed_subset import fringe_opposed_subset as fop


class fringe:
    __slots__ = ['fops']

    def __init__(self, h=None):
        self.fops = deque() if h is None else deque([fop(h)])

    def __len__(self):
        return len(self.fops)

    def __lt__(self, other):
        if not isinstance(other, fringe):
            return NotImplemented
        diff = self.L.l_lo - other.L.l_lo
        if diff != 0:
            return diff < 0
        return self.H.l_hi < other.H.l_hi

    def __repr__(self):
        return ('\33[1m\33[91m{\33[0m' +
                ' '.join([repr(c) for c in self.fops]) +
                '\33[91m\33[1m}\33[0m')

    @property
    def H(self):
        return self.fops[0]

    @property
    def L(self):
        return self.fops[-1]

    def merge(self, other):
        other._merge_t_alike_edges()
        self._merge_t_opposite_edges_into(other)
        if not self.H.right:    # self is one_sided
            self._align_duplicates(other)
        else:
            self._make_onion_structure(other)
        if other.H.left:
            self.fops.extendleft([other.H])

    def _merge_t_alike_edges(self):
        if self.H.right:
            raise Exception
        for f in islice(self.fops, 1, len(self)):
            if f.right:
                raise Exception
            self.H.left.extend(f.left)
        self.fops = deque([self.fops[0]])

    def _merge_t_opposite_edges_into(self, other):
        while (not self.H.right and self.H.l_hi > other.H.l_lo):
            other.H.right.extend(self.H.left)
            self.fops.popleft()

    def _align_duplicates(self, other):
        if self.L.l_hi == other.H.l_lo:
            other.H.left.pop()
            if (not other.H.left or (other.H.right and
                                     other.H.l_lo > other.H.r_lo)):
                other.H.c[0], other.H.c[1] = other.H.c[1], other.H.c[0]

    def _make_onion_structure(self, other):
        lo, hi = (0, 1) if self.H.l_hi < self.H.r_hi else (1, 0)
        if other.H.l_lo < self.H.c[lo][0]:
            raise Exception
        elif other.H.l_lo < self.H.c[hi][0]:
            self.H.c[lo].extendleft(reversed(other.H.left))
            self.H.c[hi].extendleft(reversed(other.H.right))
            other.H.left.clear()
            other.H.right.clear()

    def prune(self, dfs_height):
        while (self.fops and self.H.left and self.H.l_hi >= dfs_height):
            self.H.left.popleft()
            if not self.H.left and not self.H.right:
                self.fops.popleft()
        while (self.fops and self.H.right and self.H.r_hi >= dfs_height):
            self.H.right.popleft()
        if self.fops and not self.H.left:
            if self.H.right:
                self.H.c[0], self.H.c[1] = self.H.c[1], self.H.c[0]
            else:
                self.fops.popleft()

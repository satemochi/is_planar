from itertools import islice
from collections import deque
from fringe_opposed_subset import fringe_opposed_subset as fop


class fringe:
    __slots__ = ('fops')

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
        else:
            return self.H.l_hi < other.H.l_hi

    def __eq__(self, other):
        if not isinstance(other, fringe):
            return NotImplemented
        return self.L.l_lo == other.L.l_lo

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
        assert(self.fops and other.fops)
        assert(self < other or self == other)
        assert(all(f.last_of_left_is_lowest() for f in other.fops))
        assert(all(f.last_of_right_is_lowest() for f in other.fops))
        if not other._oneSided():
            return False

        while (not self.H.right and self.H.l_hi > other.H.l_lo):
            other.H.right.extend(self.H.left)
            self.fops.popleft()

        if not self.H.right:
            if self.L.l_hi == other.H.l_lo:
                other.H.left.pop()
                if (not other.H.left or (other.H.right and
                                         other.H.l_lo > other.H.r_lo)):
                    other.H.c[0], other.H.c[1] = other.H.c[1], other.H.c[0]
        else:
            lo, hi = (0, 1) if self.H.l_hi < self.H.r_hi else (1, 0)
            if other.H.l_lo < self.H.c[lo][0]:
                return False
            elif other.H.l_lo < self.H.c[hi][0]:
                self.H.c[lo].extendleft(other.H.left)
                self.H.c[hi].extendleft(other.H.right)
                other.H.left.clear()
                other.H.right.clear()

        if other.H.left:
            self.fops.extendleft([other.H])

        assert(all(f.last_of_left_is_lowest() for f in self.fops))
        assert(all(f.last_of_right_is_lowest() for f in self.fops))
        return True

    def _oneSided(self):
        if self.H.right:
            return False
        for f in islice(self.fops, 1, len(self)):
            if f.right:
                return False
            self.H.left.extend(f.left)
        self.fops = deque([self.fops[0]])
        return True

    def prune(self, dfs_height):
        while (self.fops and self.H.left and self.H.l_hi >= dfs_height-1):
            if len(self.H.left) == 1:
                self.fops.popleft()
            else:
                self.H.left.popleft()
        while (self.fops and self.H.right and self.H.r_hi >= dfs_height-1):
            self.H.right.popleft()

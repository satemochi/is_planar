from itertools import islice
from collections import deque
from fringe_opposed_subset import fringe_opposed_subset as fop


class fringe:
    """ The class of a fringe of a tree edge

    This class maintains fringes of a tree edge (x, y).

    The definition of the fringe can be found in the following literature;

        H. de Fraysseix and P. O. de Mendez. (2012).
        "Tremaux trees and planarity",
        European Journal of Combinatorics, 33(3): 279-293.

    Roughly, from Definition 2.2:
        The fringe Fringe(e) of an edge e = (x, y) is defined by

        .. math:: \mathrm{Fringe}(e) = \{f in E \setminus T ~:~
                          f \succeq e  and \mathrm{low}(f) \prec x\}.
        
            - E : edge set of a given graph
            - T : tree edge set of a DFS tree (T is subset of E)
            - f : any back edge
            - low : destination vertex
            - binary relations compare between heights or traversal orders.

        ...
        In other words, the fringe of a tree edge e = (x, y) is the set of
        all back edges linking a vertex in the subtree rooted at y and 
        a vertex strictly smaller than x.
        ...

    !!!Caution!!!
        The above is excerpt from the literature, we have a little correction.
        We omit "strictly", thus our fringe contains back edges incoming to x.

    In general, we don't care about the order of heights of back edges.
    However, when merged fringe is constructed from upper fringes, which are
    of tree edges outgoing from y, upper fringes or list of fringe-opposed
    subsets are expected in the order from lower to higher.
    The criterion of the comparison is defined at __lt__.

    Attributes
    ----------
    H
    L
    fops : deque of fringe_opposed_subset
        The fringe of a tree edge (x, y) mainly consists of
        the fringe-opposed subsets for each tree edges outgoing from y.
        More strictly, it also contains one-sided single fringe-opposed
        subsets for each back edge outgoing from y.

        The number of elements in fops is less than or equal to
            the number of tree edges outgoing from y
             + the number of back edges outgoing from y.

    Methods
    _______
    merge(other)
        Merge other fringe into self one.

    prune(dfs_height)
        Prune back edges whose DFS height greater than or
        equal to dfs_height.
    """

    __slots__ = ['fops']

    def __init__(self, h=None):
        self.fops = deque() if h is None else deque([fop(h)])

    def __len__(self):
        return len(self.fops)

    def __lt__(self, other):
        """
        The ordering criterion for fringes

        We intend to pack as many back edges as possible into the left side 
        of a fringe-opposed subset. So, we make much account of
        the lower/higher LEFT low/high back edges.
        An important thing is which fringe is nested in the other.
        """

        diff = self.L.l_lo - other.L.l_lo
        if diff != 0:
            return diff < 0
        return self.H.l_hi < other.H.l_hi

    def __repr__(self):
        """ print in terminal with colors 
            see https://stackoverflow.com/questions/287871/
        """
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
        """
        merge other fringe into self one

        Parameters
        ----------
        other : fringe
            a fringe merged into self.
            This is the part of the subtree rooted at y, or back edges
            outgoing from y.

        Notes
        -----
        A number of preconditions:
            - Both self and other have at least one fringe-opposed subset
              with at least one back edge.
              i.e., 'len(self) > 0' and 'len(other) > 0'
            - self <= other. 
              This implies that the lowest lowpoint of self is lower than
              the others. In other words, other is nested into the lowest 
              back edge of fringe-opposed subset of self.

              This assumption have a number of advantages. 
              - We can immediately detect non-planarity, if other have a
                two-sided fringe-opposed subset.
                So, we can detect Kuratowski subgraphs from two components;
                    - fundamental cycle of a back edge returning the
                      lowest lowpoint in self,
                    - this two-sided fringe-opposed subset.
              - and so on...
        """

        other._merge_t_alike_edges()
        self._merge_t_opposite_edges_into(other)
        if not self.H.right:    # self is one_sided
            other._align_duplicates(self.L.l_hi)
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

    def _align_duplicates(self, dfs_h):
        if self.H.l_lo == dfs_h:
            self.H.left.pop()
            if (not self.H.left or (self.H.right and
                                    self.H.l_lo > self.H.r_lo)):
                self.H.c[0], self.H.c[1] = self.H.c[1], self.H.c[0]

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
        """
        Prune back edges whose DFS height greater than or
        equal to dfs_height.

        Parameters
        ----------
        dfs_height : int
            To be used as a threshold whether is a back edge survived.
        """

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

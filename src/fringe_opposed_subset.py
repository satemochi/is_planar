from collections import deque


class fringe_opposed_subset:
    """ The class of the fringe-opposed subset

    Roughly speaking, a fringe-opposed subset maintain the property of
    the T-opposite/T-alike relations for traversed back edges.
    The T-opposite (T-alike) means that two back edges will be on different
    (same) sides of the DFS-tree in every planar drawing.

    The detailed definition for fringe-opposed subsets can be reffered;

        H. de Fraysseix and P. O. de Mendez. (2012).
        "Tremaux trees and planarity",
        European Journal of Combinatorics, 33(3): 279-293.

    Attributes
    ----------
    c : list of deque of int
        The pair of left side back edges and right side ones.
        The left side back edges and right ones are T-opposed each other.

        This does not maintain a back edge (x, y) itself, but the DFS-height
        of the termination (lowpoint) y.

        The lowest height of back edges in the left is lower than the right
        ones as far as possible.

        Each side have been ordered according to DFS height. The head has
        the highest lowpoint height, and the tail has the lowest.
        Back edges are expired from higher ones. T-alike back edges are
        concatenated from higher ones. And so on... Therefore, we use deque.
    """

    __slots__ = ['c']

    def __init__(self, h):
        self.c = [deque([h]), deque()]

    def __repr__(self):
        """ print in terminal with colors 
            see https://stackoverflow.com/questions/287871/
        """
        return ('\33[1m\33[90m(\33[0m' + str(list(self.c[0])) +
                ', ' + str(list(self.c[1])) + '\33[1m\33[90m)\33[0m')

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

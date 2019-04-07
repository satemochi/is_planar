from collections import defaultdict
from itertools import islice
from fringe import fringe

__all__ = ['is_planar']


def is_planar(g):
    """
    The top of the left-right algorithm for testing planarity of graphs.

    We can refer its basic concepts and notations in [1]_.

    Parameters
    ----------
    g : networkx.Graph
        A simple undirected graph of NetworkX.

        If g has four methods size(), order(), v in g, and g[v], then
        is_planar does not require NetworkX.

            1. size() : returns the number of edges
            2. order() : returns the number of vertices
            3. v in g: returns all vertices in g as iterable
            4. g[v] : returns a list or iterable of the neighbors of a vertex v

    Returns
    -------
    result : bool
        result is true if the graph is planar.

    References
    ----------
    .. [1] H. de Fraysseix and P. O. de Mendez (2012).
           Tremaux trees and planarity.
           Europ. J. Combin., 33(3):279-293.
           https://core.ac.uk/download/pdf/82483715.pdf
    """

    if g.size() < 9 or g.order() < 5:
        return True
    if g.size() > 3 * g.order() - 6:
        return False
    visited = defaultdict(lambda: False)
    for v in g:
        if not visited[v]:
            visited[v] = True
            if not lr_algorithm(g, v, visited):
                return False
    return True


def lr_algorithm(g, root, visited):
    """
    The framework of depth-first search (DFS) in the left-right algorithm.

    Parameters
    ----------
    g : networkx.Graph
        A simple undirected graph of NetworkX.

    root : any hashable or immutable variable
        A vertex for starting DFS, or DFS root.

    visited : defaultdict
        To be used as a checklist visiting vertices. So lr_algorithm assumes
        that unvisited vertices are initialized with False. It is not
        necessary to use defaultdict, else dict such as a map from V to
        {True, False} may be appropriative. However, since lr_algorithm
        immediately terminates as soon as finding a violation against
        the left-right criterion, we have specified defaultdict.

        Noting that visited is the call by sharing, it is also accessed for
        checking all components in graph g are completely searched.

    Returns
    -------
    result : bool
        result is true if the graph is planar.
    """

    fringes = [[]]
    dfs_heights = defaultdict(lambda: 0)
    dfs_stack = [(root, iter(g[root]))]
    while dfs_stack:
        x, children = dfs_stack[-1]
        try:
            y = next(children)
            if visited[y]:
                if dfs_heights[x] > dfs_heights[y]:  # back edge
                    fringes[-1].append(fringe(dfs_heights[y]))
            else:   # tree edge
                visited[y] = True
                fringes.append([])
                dfs_heights[y] = dfs_heights[x] + 1
                dfs_stack.append((y, iter([u for u in g[y] if u != x])))
        except StopIteration:
            dfs_stack.pop()
            if len(fringes) > 1:
                try:
                    merge_fringes(fringes, dfs_heights[dfs_stack[-1][0]])
                except Exception as e:
                    return False
    return True


def merge_fringes(fringes, dfs_height):
    """
    merge fringes and prune back edges

    Parameters
    ----------
    fringes : list of lists of fringes
        The stack of fringes of all tree edges have been traversed. Except of
        the top, each list of fringes is under construction.

    dfs_height: int
        Newly created fringes have no back edges which have DFS heigh greater
        than or equal to dfs_height.
    """

    mf = get_merged_fringe(fringes[-1])
    fringes.pop()
    if mf is not None and mf.fops:
        fringes[-1].append(mf)
        for f in fringes[-1]:
            f.prune(dfs_height)
            if not f.fops:
                fringes[-1].pop()


def get_merged_fringe(upper_fringes):
    """
    merge (upper) fringes

    In order to construct the fringe of the tree edge (x, y) that is top of
    dfs_stack, this function merges all fringes of tree edges outgoing from y.

    Parameters
    ----------
    upper_fringes : list of fringes
        upper_fringes consists of all fringes of tree edges outgoing from y.
        Further, for each back edge e in upper_fringes, the DFS height of
        low-point low(e) is lower than dfs_heights[y].

    Returns
    -------
    new_fringe : fringe
        new_fringe is the merged fringe if upper_fringes do not contain any
        violation against the left-right criterion.
    """

    if len(upper_fringes) > 0:
        upper_fringes.sort()
        new_fringe = upper_fringes[0]
        for f in islice(upper_fringes, 1, len(upper_fringes)):
            new_fringe.merge(f)
        return new_fringe

is_planar
====

A python code which implements the LR-algorithm for testing planarity of given graphs.

## Description
**is_planar**  is a python code of the left-right algorithm that tests
the planarity of given graphs in linear time.

More detailed accurate descriptions of the LR-algorithm can be referred
[Left-right planarity test: wikipedia](https://en.wikipedia.org/wiki/Left-right_planarity_test) or the literature [1, 2, 3].

**is_planar** can determine the planarity of a given graph with a
computational complexity proportional to at most one depth-first search.
Not only is its brevity easy to understand, the LR-algorithm is also known
to be the fastest of some linear time algorithms [4].

**is_planar** is an alpha version.
If consistent planarity test is the purpose, then we recommend
[check_planarity](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.planarity.check_planarity.html) of
[networkx](https://networkx.github.io) and
[boyer_myrvold_planar_test.hpp](https://www.boost.org/doc/libs/1_37_0/boost/graph/boyer_myrvold_planar_test.hpp) of
[BGL](https://www.boost.org/doc/libs/1_37_0/libs/graph/doc/planar_graphs.html).

**is_planar** conforms to the GPL license, as it is a good reference for the 
[Pigale](http://pigale.sourceforge.net) source code.

## Requirements
- python 2.7
- [networkx 2.2](https://networkx.github.io)

## License
[GPL 2.0](https://github.com/satemochi/is_planar/blob/master/LICENSE)

## Todo
- API / Comments
    - docstring 
- Testing
    - Do unit tests for each modules
    - Do tests with all DFS orderings for a given graph
    - Do random generations of planar graphs
    - Do enumeration of small planar graphs
- Functions
    - Computations for planar embeddings or Kuratowski subgraphs.
    - Plane drawings (Tutte embeddings and so on)
    - Boyer-Myrvold algorithm [5]

## References
1. H. de Fraysseix and P. O. de Mendez. (2012). "**Trémaux trees and planarity**", European Journal of Combinatorics, 33 (3): 279–293.
1. H. de Fraysseix, P. O. de Mendez, and P. Rosenstiehl, (2006). "**Trémaux Trees and Planarity**", International Journal of Foundations of Computer Science, 17 (5): 1017–1030.
1. U. Brandes, (2009). "**The left-right planarity test**", [pdf](http://www.inf.uni-konstanz.de/algo/publications/b-lrpt-sub.pdf).
1. M. J. Boyer, P. F. Cortese, M. Patrignani, and G. D. Battista, (2003), "**Stop minding your P's and Q's: implementing a fast and simple DFS-based planarity testing and embedding algorithm**", Proc. 11th Int. Symp. Graph Drawing (GD '03), Lecture Notes in Computer Science, 2912, Springer-Verlag, pp. 25–36
1. M. J. Boyer and  W. J. Myrvold. (2004). "**On the cutting edge: simplified O(n) planarity by edge addition**", Journal of Graph Algorithms and Applications, 8 (3): 241–273.

is_planar
====

A python code which implements the left-right algorithm for testing planarity
of given graphs.

## Description
- **is_planar**  is a pure python code of the left-right algorithm [1, 2, 3]
that tests the planarity of given graphs in linear time.
The brevity is not only easy to understand,
but also known to be the fastest among some linear time algorithms [4].

- **is_planar** conforms to the GPL license, as it is a good reference for the 
[Pigale](http://pigale.sourceforge.net) source code.
Thus, our left-right algorithm should be called as the
[Daniel Ford](https://www.researchgate.net/profile/Daniel_Ford6)'s algorithm.

- **is_planar** is an alpha version.
If consistent planarity test is the purpose, we recommend
[check_planarity](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.planarity.check_planarity.html) of
[NetworkX](https://networkx.github.io) and
[boyer_myrvold_planar_test.hpp](https://www.boost.org/doc/libs/1_37_0/boost/graph/boyer_myrvold_planar_test.hpp) of
[BGL](https://www.boost.org/doc/libs/1_37_0/libs/graph/doc/planar_graphs.html).


## Features
- **is_planar** is a short script.
The SLOC is at most 160 lines while keeping permissible cyclomatic complexity
and maintainability index,
according to [radon](https://radon.readthedocs.io/en/latest/),
the code metrics evaluation tool.

- **is_planar** have been tested by **all connected simple graphs** up to
10 vertices, and passed.
We would borrow the graph data from
[Combinatorial Data](https://users.cecs.anu.edu.au/~bdm/data/graphs.html).
Further, we would use [nauty Traces](http://pallini.di.uniroma1.it) / 
[pynauty](https://web.cs.dal.ca/~peter/software/pynauty/html/)
for constructing a cheat sheet of planar graphs (see tests/g/bit_setter.py).

- **is_planar** is about 777% faster than [check_planarity](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.planarity.check_planarity.html) of [NetworkX](https://networkx.github.io)
if the purpose is just tests of its planarity.
It may be unfair to compare with is_planar,
since check_planarity can compute planar embeddings and extract Kuratowski
subgraphs as byproducts.

However, is_planar have tiny advantages, see misc/vs_check_planarity.py.
![vs_check_planarity](https://github.com/satemochi/is_planar/blob/master/misc/vs_check_planarity_1.png "logging on April 22nd, 2019.")
Log-scale! Cheating!? :-p

## Requirements
- python 2.7 / 3.7
- [networkx 2.2 / 2.3](https://networkx.github.io)

## License
[GPL 2.0](https://github.com/satemochi/is_planar/blob/master/LICENSE)

## Todo
- API / Comments
    - docstring
- Tests
    - Do efficient generation of all DFS orderings. The current generator is
      naive, and cannot allow more than 10 vertices. Now we consider to
      implement ZDDs with frontier approachs for more vertices with reasonable
      processing time.
    - Do generation randomly large planar graphs. Now we consider to borrow
      the Boltzmann sampler [5].
- Functions
    - Computations for planar embeddings or Kuratowski subgraphs.
    - Plane drawings (Tutte embeddings and so on)
    - Boyer-Myrvold algorithm [6]

## References
1. H. de Fraysseix and P. O. de Mendez. (2012). "**Trémaux trees and planarity**", European Journal of Combinatorics, 33 (3): 279–293.

1. H. de Fraysseix, P. O. de Mendez, and P. Rosenstiehl, (2006). "**Trémaux Trees and Planarity**", International Journal of Foundations of Computer Science, 17 (5): 1017–1030.

1. U. Brandes, (2009). "**The left-right planarity test**", [pdf](http://www.inf.uni-konstanz.de/algo/publications/b-lrpt-sub.pdf).

1. M. J. Boyer, P. F. Cortese, M. Patrignani, and G. D. Battista, (2003), "**Stop minding your P's and Q's: implementing a fast and simple DFS-based planarity testing and embedding algorithm**", Proc. 11th Int. Symp. Graph Drawing (GD '03), Lecture Notes in Computer Science, 2912, Springer-Verlag, pp. 25–36

1. E. Fusy, (2009), "**Uniform random sampling of planar graphs in linear time**", Random Structures and Algorithms 35(4): 464-522. [site](http://www.lix.polytechnique.fr/Labo/Eric.Fusy/)

1. M. J. Boyer and  W. J. Myrvold. (2004). "**On the cutting edge: simplified O(n) planarity by edge addition**", Journal of Graph Algorithms and Applications, 8 (3): 241–273.

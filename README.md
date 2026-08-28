is_planar
====

This is a Python code that implements the left-right algorithm for testing graph planarity.


## Description
- **is_planar**  is a pure Python code for the [left-right planarity test](https://en.wikipedia.org/wiki/Left-right_planarity_test) [1].
Its brevity makes it easy to understand and 
one of the fastest among some linear-time algorithms.

- **is_planar** is licensed under the GPL 2.0 because
some lines reference from the [Pigale](http://pigale.sourceforge.net) library.


## Requirements
- [Python](https://www.python.org)
- [NetworkX](https://networkx.github.io)


## Usage
```python
>>> from is_planar import is_planar
>>> import networkx as nx
>>> is_planar(nx.frucht_graph())
True
>>> is_planar(nx.petersen_graph())
False
```


## Features
- **is_planar** is short.
It has about 170 lines of code while maintaining 
permissible cyclomatic complexity and maintainability index.
We evaluated it with [Radon](https://radon.readthedocs.io/en/latest/).

- **is_planar** has been tested with **all connected simple graphs** up to
ten vertices (about 12 million graphs), and has passed.
We would borrow the graph data from
[Combinatorial Data](https://users.cecs.anu.edu.au/~bdm/data/graphs.html).


## References
1. H. de Fraysseix and P. O. de Mendez. (2012). "**Trémaux trees and planarity**", European Journal of Combinatorics, 33 (3): 279–293.


## License
[GPL 2.0](https://github.com/satemochi/is_planar/blob/master/LICENSE)

Copyright (c) 2019-2026, 
[satemochi](satemochi1@yahoo.co.jp) <br/>
All rights reserved.

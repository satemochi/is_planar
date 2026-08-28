is_planar
====

This is a Python code that implements the left-right algorithm for testing graph planarity.


## Description
- **is_planar**  is a pure Python code for the [left-right planarity test](https://en.wikipedia.org/wiki/Left-right_planarity_test),
due to [de Fraysseix](http://fraysseix.free.fr/$0) and
[Ossona de Mendez](https://en.wikipedia.org/wiki/Patrice_Ossona_de_Mendez) [1].

- **is_planar** is licensed under the GPL 2.0 because
some lines reference from the [PIGALE](http://pigale.sourceforge.net) library.

- The primary purpose of **is_planar** is to enhace the understanding of linear-time planarity tests based on [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search$0).




## Requirements
- [Python](https://www.python.org)
- [NetworkX](https://networkx.github.io)

`is_planar` is not [nx.is_planar](https://networkx.org/documentation/stable/reference/algorithms/planarity.html); they are completely different.
We only use NetworkX for graph containers, since its API is very wonderful.

## Installation
1. Download `is_planar.py` file, and
1. Copy and place it in any directory included in the `PYTHONPATH` variable.



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
- **is_planar** is short and carefully designed.
It has about 170 lines of code while maintaining
permissible cyclomatic complexity and maintainability index,
according to the [Radon](https://radon.readthedocs.io/en/latest/).
However, the names of each function/method may need more refinement.

The result on maintainability index of `is_planar.py`.
```console
$ radon mi -s is_planar.py 
is_planar.py - A (33.17)
```


- The `is_planar` function has been tested on **all connected simple graphs** with up to
10 vertices (approximately 12 million graphs in total), and has passed.
We would borrow the graph data from the 
[Combinatorial Data](https://users.cecs.anu.edu.au/~bdm/data/graphs.html).

You can try our exhaustive tests. If the number of vertices is up to 9 (0.3 million graphs), then it may finish in 5 seconds, but we cannot be sure. Do this after fetching `graph*c.g6` ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/$0)) from the site, and place in the directory `tests/g`. Then, enter the following commands at the top of the `is_planar` directory:

```console
$ ls tests/g
bit_setter.py         graph7c.g6            planar_conn.6.pkl
bit_setter_serial.py  graph8c.g6            planar_conn.7.pkl
graph10c.g6           graph9c.g6            planar_conn.8.pkl
graph6c.g6            planar_conn.10.pkl    planar_conn.9.pkl

$ python -m pytest
```


## References
1. H. de Fraysseix and P. Ossona de Mendez. (2012). "**Trémaux trees and planarity**", European Journal of Combinatorics, 33 (3): 279–293.


## License
[GPL 2.0](https://github.com/satemochi/is_planar/blob/master/LICENSE)

---
Copyright (c) 2019-2026, <br/>
satemochi: [satemochi1@yahoo.co.jp](satemochi1@yahoo.co.jp) <br/>
All rights reserved.

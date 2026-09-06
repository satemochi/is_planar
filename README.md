is_planar
====

This is a Python code that implements the left-right algorithm for testing graph planarity.


## Description
- **is_planar**  is a pure Python code for the [left-right planarity test](https://en.wikipedia.org/wiki/Left-right_planarity_test),
due to [de Fraysseix](http://fraysseix.free.fr/) and
[Ossona de Mendez](https://en.wikipedia.org/wiki/Patrice_Ossona_de_Mendez) [1].

- **is_planar** is licensed under the GPL 2.0 because
some lines reference from the [PIGALE](http://pigale.sourceforge.net) library.

- The primary purpose of **is_planar** is to enhace the understanding of linear-time planarity tests based on [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search).




## Requirements
- [Python](https://www.python.org)
- [NetworkX](https://networkx.github.io)

`is_planar` is not [nx.is_planar](https://networkx.org/documentation/stable/reference/algorithms/planarity.html); they are completely different.
We only use NetworkX for graph containers, since its API is very wonderful.

## Installation
1. Download `is_planar.py` file, and
1. Copy and place it in any directory included in `sys.path` or the `PYTHONPATH` variable.



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

For example, the result on maintainability index and cyclomatic complexity
of `is_planar.py` is as follow:
```console
$ radon mi -s is_planar.py 
is_planar.py - A (33.17)

$ radon cc is_planar.py
is_planar.py
    F 20:0 __lr_algorithm - B
    M 121:4 fringe.prune - B
    F 6:0 is_planar - B
    C 59:0 fringe - A
    M 88:4 fringe.__merge_t_alike_edges - A
    M 107:4 fringe.__swap_side - A
    M 111:4 fringe.__make_onion_structure - A
    F 43:0 __merge_fringes - A
    F 50:0 __get_merged_fringe - A
    M 78:4 fringe.merge - A
    M 97:4 fringe.__merge_t_opposite_edges_into - A
    M 135:4 fringe.__lr_condition - A
    M 62:4 fringe.__init__ - A
    M 65:4 fringe.__lt__ - A
    M 102:4 fringe.__align_duplicates - A
    C 140:0 fop - A
    M 71:4 fringe.H - A
    M 75:4 fringe.L - A
    M 143:4 fop.__init__ - A
    M 147:4 fop.left - A
    M 151:4 fop.right - A
    M 155:4 fop.l_lo - A
    M 159:4 fop.l_hi - A
    M 163:4 fop.r_lo - A
    M 167:4 fop.r_hi - A
```

The result on raw of ``is_planar.py`` is as follows: 
This implies that the logical lines are at most 140 and that
renaming the sentences (i.e., the ``@property`` attributes)
takes around 30 lines.
```console
$ radon raw is_planar.py
is_planar.py
    LOC: 168
    LLOC: 136
    SLOC: 137
    Comments: 3
    Single comments: 0
    Multi: 0
    Blank: 31
    - Comment Stats
        (C % L): 2%
        (C % S): 2%
        (C + M % L): 2%
```



- `is_planar` function has been tested on **all connected simple graphs** with
up to 10 vertices (approximately 12 million graphs in total), and has passed.
We would borrow the graph data from the 
[Combinatorial Data](https://users.cecs.anu.edu.au/~bdm/data/graphs.html).

You can try our exhaustive tests. We cannot say for certain, but it might take around 30 minutes to complete. Do this after fetching `graph*c.g6` ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)) from the site, and place in the directory `tests/g`. Then, enter the following commands at the top of the `is_planar` directory:

```console
$ ls tests/g
bit_setter.py         graph7c.g6            planar_conn.6.pkl
bit_setter_serial.py  graph8c.g6            planar_conn.7.pkl
graph10c.g6           graph9c.g6            planar_conn.8.pkl
graph6c.g6            planar_conn.10.pkl    planar_conn.9.pkl

$ python -m pytest
============================= test session starts ==============================
platform darwin -- Python 3.13.5, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/satemochi/progs/is_planar
collected 65 items

tests/test_all_simple.py .....                                           [  7%]
tests/test_dfs_order.py ....s.                                           [ 16%]
tests/test_named_graphs.py ............................................. [ 86%]
.........                                                                [100%]

================== 64 passed, 1 skipped in 1410.70s (0:23:30) ==================
```


## Tips

Our implementation still seems difficult to understand.
Therefore, we have prepared a fundamental step: two-edge connectivity
(see [examples/is_two_edge_connected/](https://github.com/satemochi/saaaaah/blob/master/is_planar/examples/is_two_edge_connected/)).
This example shows how to use ``fringe`` and ``fops`` classes.

The bridge finding algorithm (due to Hopcroft and Tarjan) can be found in the
[Wikipedia](https://en.wikipedia.org/wiki/Biconnected_component) article.
Metaphorically speaking,
this algorithm just observes the race of
"the lowest fringe" against "backtracking".


**is_planar** has the same framework as ``is_two_edge_connected`` function.
Once we understood the [left-right planarity condition](https://en.wikipedia.org/wiki/Left-right_planarity_test),
we realized that our implementation was extremely simple.



## References
1. H. de Fraysseix and P. Ossona de Mendez. (2012). "**Trémaux trees and planarity**", European Journal of Combinatorics, 33 (3): 279–293.


## License
[GPL 2.0](https://github.com/satemochi/is_planar/blob/master/LICENSE)

---
Copyright (c) 2019-2026, <br/>
satemochi: [satemochi1@yahoo.co.jp](satemochi1@yahoo.co.jp) <br/>
All rights reserved.

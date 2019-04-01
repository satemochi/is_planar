is_planar
====

A python code which implements the LR-algorithm for testing planarity of given graphs.

## 説明
**is_planar** は、グラフの平面性判定を線形時間で解決する LR-アルゴリズムの python コードです。

アルゴリズムの詳細は、[Left-right planarity test: wikipedia](https://en.wikipedia.org/wiki/Left-right_planarity_test)や参考文献 [1, 2, 3] をご覧ください。

**is_planar** は、たかだか1回の深さ優先探索に比例する計算量で、与えられたグラフの平面性を判定することができます。その簡潔さはアルゴリズム理解が容易なだけでなく、いくつかある線形時間アルゴリズムのなかでも最速であることが知られています [4]。

**is_planar** はアルファ版です。堅実な平面性判定が目的なら [networkx](https://networkx.github.io) の [check_planarity](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.planarity.check_planarity.html) や、[BGL](https://www.boost.org/doc/libs/1_37_0/libs/graph/doc/planar_graphs.html) の [boyer_myrvold_planar_test.hpp](https://www.boost.org/doc/libs/1_37_0/boost/graph/boyer_myrvold_planar_test.hpp) などのご利用をお勧めいたします。

**is_planar** は、[Pigale](http://pigale.sourceforge.net) のソースコードを大いに参考にしているため GPL ライセンスに準拠します。

**is_planar** は、頂点数 10 までの全ての連結な平面的グラフでテストし、パスしています。平面グラフの情報は下記のサイトからお借りしました。
[Combinatorial Data](https://users.cecs.anu.edu.au/~bdm/data/graphs.html).

## 利用要件
- python 2.7
- [networkx 2.2](https://networkx.github.io)

## ライセンス
[GPL 2.0](https://github.com/satemochi/is_planar/blob/master/LICENSE)

## Todo
- API / コメント整備
    - docstring 
- 機能追加
    - 平面埋め込みの計算
    - Kuratowski 部分グラフの抽出
    - 平面描画 (Tutte 埋め込みなど)
    - Boyer-Myrvold アルゴリズム[5] の実装

## 参考文献
1. H. de Fraysseix and P. Ossona de Mendez. (2012). "**Trémaux trees and planarity**", European Journal of Combinatorics, 33 (3): 279–293.
1. H. de Fraysseix, P. Ossona de Mendez, and P. Rosenstiehl, (2006). "**Trémaux Trees and Planarity**", International Journal of Foundations of Computer Science, 17 (5): 1017–1030.
1. U. Brandes, (2009). "**The left-right planarity test**", [pdf](http://www.inf.uni-konstanz.de/algo/publications/b-lrpt-sub.pdf).
1. M. J. Boyer, P. F. Cortese, M. Patrignani, and G. D. Battista, (2003), "**Stop minding your P's and Q's: implementing a fast and simple DFS-based planarity testing and embedding algorithm**", Proc. 11th Int. Symp. Graph Drawing (GD '03), Lecture Notes in Computer Science, 2912, Springer-Verlag, pp. 25–36
1. M. J. Boyer and  W. J. Myrvold. (2004). "**On the cutting edge: simplified O(n) planarity by edge addition**", Journal of Graph Algorithms and Applications, 8 (3): 241–273.

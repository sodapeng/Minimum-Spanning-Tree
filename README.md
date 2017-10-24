
## Implement Prim's and Kruskal's algorithm to find a minimum spanning tree.
A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight. 

### Prim's Algorithm:
An greedy algorirthm that finds a minimum spanning tree for a weighted undirected graph. The algorithm operates by building this tree one vertex at a time, from an arbitrary starting vertex, at each step adding the cheapest possible connection from the tree to another vertex.

### Kruskal's algorithm:
Another greedy algorirthm that finds a minimum spanning tree for a weighted undirected graph. The algorithm operates by first create a graph F with all vertex in the given graph, where each vertex in the graph is a spearate tree, and then create a set S with all edges in the given graph. At each step, remove an edge with minimum weight from S, and if the removed edges connects two different trees in F, then combine these two trees, terminate when S is not empty and F is not yet spanning.

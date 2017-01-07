import random

# Generate random weighted graphs as instances of MST
def random_weighted_graph(number_nodes=10,probability=0.5,max_weight=100):
    # Node set is {0,1,...,number_nodes-1}
    node_set = {u for u in range(number_nodes)}
    # Edge set is a dictionary of sets, one set per node
    # Each entry in a set is a tuple of a neighbor of that node and
    #    the edge weight
    edge_set = {u:set() for u in node_set}
    for u in node_set:
        for v in node_set:
            if u < v:
                random_probability = random.random()
                if random_probability < probability and probability > 0.0:
                    # There is an edge (u,v)=(v,u)
                    # Need the edge weight
                    weight = random.randrange(1,max_weight)
                    edge_set[u].add((v,weight))
                    edge_set[v].add((u,weight))
    return (node_set,edge_set)

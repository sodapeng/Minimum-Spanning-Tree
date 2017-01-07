#!/usr/bin/env python3
# Copyright (c) 2016 Liangpeng Zhuang. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#asas

"""
This module solves CS 5045 Homework Assignment 9.
See assignment for details.
"""

import argparse
from heapq import heappop, heappush
import logging
import random
from random_graph import *
import sys

# Listing 7-5: Prim's algorithm for MST
def prim(G,s):
    V, E = G
    weight = 0          # Accumulate weight of MST
    P = {}              # Empty dictionary to store Prim tree
    Q = [(0,None,s)]    # Initialize the priority queue
    T = set()           # Set of edges in resulting tree
    while Q:
        w, p, u = heappop(Q)
        if u in P:
            continue
        weight += w
        P[u] = p
        if p is not None:
            T.add((p,u))
        neighbors = E[u]
        for v,w in neighbors:
            heappush(Q,(w,u,v))
    return (P,T,weight)

# Listing 7-4: Kruskal's algorithm for MST
def find(C,u):
    while C[u] !=u:
        u = C[u]
    return u

def union(C,R,u,v):
    u, v = find(C,u), find(C,v)
    if R[u] > R[v]:
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:
        R[v] += 1
        
def kruskal(G):
    V, E = G
    weight = 0                  # Accumulate weight of MST
    T = set()
    E_edges = []
    for u in E:
        for v in E[u]:
            E_edges.append((v[1],u,v[0]))
    C = {u:u for u in E}
    R = {u:0 for u in E}
    for weight_uv, u, v in sorted(E_edges):
        if find(C,u) != find(C,v):
            T.add((u,v))
            union(C,R,u,v)
            weight += weight_uv
    return (T,weight)

def main():
    """
    This function directs the parsing of the command line arguments,
    calling Prim's and Kruskal's, and the construction of the output file.
    Use argparse to parse the command line arguments.
    Use logging to save progress to a logging file.
    """
    logging.basicConfig(filename="homework9.log",filemode="w",
        level=logging.INFO,format="%(levelname)s: %(asctime)s: %(message)s")
    logging.info("Starting homework9.py")
    argparser = argparse.ArgumentParser(
        description="Execute MST algorithms for Assignment 9.")
    argparser.add_argument("output_file", metavar="output_file",
        help="the output file name")
    argparser.add_argument("-n", metavar="number_nodes", default=10,
        help="Number of nodes in random graph")
    argparser.add_argument("-p", metavar="probability", default=0.5,
        help="Probability of an edge")
    argparser.add_argument("-m", metavar="max_weight", default=100,
        help="Maximum edge weight")
    args = argparser.parse_args()
    logging.info("Arguments successfully parsed")

    # Get output file name
    output_file = args.output_file
    logging.info("Output file is {0}".format(output_file))

    # Get number of nodes in random graph
    try:
        n = int(args.n)
        if n <= 0:
            raise Exception("Number of nodes not positive")
        logging.info("Number of nodes is {0}".format(n))
    except:
        message = "Number of nodes must be a positive integer"
        print(message,file=sys.stderr)
        logging.error(message)
        sys.exit(1)     # Exit with error 1

    # Get edge probability
    try:
        p = float(args.p)
        if p < 0.0 or p > 1.0:
            raise Exception("Edge probability not between 0.0 and 1.0")
        logging.info("Edge probability is {0}".format(p))
    except:
        message = "Edge probability must be a float between 0.0 and 1.0"
        print(message,file=sys.stderr)
        logging.error(message)
        sys.exit(1)     # Exit with error 1

    # Get maximum weight
    try:
        m = int(args.m)
        if m <= 0:
            raise Exception("Maximum weight not positive")
        logging.info("Maximum weight is {0}".format(m))
    except:
        message = "Max weight must be a positive integer"
        print(message,file=sys.stderr)
        logging.error(message)
        sys.exit(1)     # Exit with error 1

    # Open output file
    try:
        output = open(output_file,"w",encoding="utf8")
    except:
        message = "Unable to open {0} for writing".format(output_file)
        print(message,file=sys.stderr)
        logging.error(message)
        sys.exit(1)	# Exit with error 1

    # Generate a random graph and pass it to MST algorithms
    G = random_weighted_graph(number_nodes=n,probability=p,max_weight=m)
    print("Graph is:\n",G,file=output)
    s = random.sample(G[0],1)[0]        # Choose a random node
    print("Random start node is",s,file=output)
    print("Running Prim's algorithm on G,s",file=output)
    logging.info("Running Prim's algorithm")
    P,T_prim,weight_prim = prim(G,s)    # Prim's algorithm
    print("P is:\n",P,file=output,sep="")
    print("T is:\n",T_prim,file=output,sep="")
    print("Total MST weight is",weight_prim,file=output)
    logging.info("Total MST weight is {0}".format(weight_prim))
    print("Running Kruskal's algorithm on G",file=output)
    logging.info("Running Kruskal's algorithm")
    T_kruskal,weight_kruskal = kruskal(G)   # Kruskal's algorithm
    print("T is:\n",T_kruskal,file=output,sep="")
    print("Total MST weight is",weight_kruskal,file=output)
    logging.info("Total MST weight is {0}".format(weight_kruskal))

    output.close()	# Good idea to close file when done
    logging.info("Successfully wrote {0}".format(output_file))

if __name__ == "__main__":
    main()
#Note: time complexity for prim and kruokal algorithm is the same theta(|E|lg|V|)
# Answer the additional questions here
#1. Yes, it is possible for prim and kruskal to return same total 
# weight but different edges. If there are multiple shortest paths, 
#prim use priority quene to select shortest path, and kruskal choose 
#shortest path according to greedy algorithms. It is possible for 
#them to choose different edges during the selection, but all lead to
#same final weight
# 2. No, it is impossible for prim and kruskal to return different weight
#but still correct. Because there is always only one minimized total weight

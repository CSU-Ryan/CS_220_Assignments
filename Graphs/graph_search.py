"""
Breadth First and Depth First Search

The objective is to write a Python program that traverses graphs in BFS
and DFS manner. BFS will determine the shortest path distance (number of
edges) from the root for each node reachable from the root. DFS will find
cycles in the graph of nodes reachable from the root. Study the lecture on
graphs, in particular graph traversals.


Some helper code is provided. Don't change it. Don't change your main,
it is used to check your code's correctness.

It is your job to implement dfs and bfs. In both dfs and bfs, visit
children of a node in left to right order, i.e., if adj is the
adjacency list of a node, visit the children as follows: for nxt in adj

Given an input file in:

a b
b c
c a d
d c

and root a

python dfbf.py in a produces:


dfbf.py
BFS
Input graph: nodeName (color, [adj list]) dictionary
a ('white', ['b'])
b ('white', ['c'])
c ('white', ['a', 'd'])
d ('white', ['c'])
Root node: a
BFS queue: (node name, distance) pairs
[('a', 0), ('b', 1), ('c', 2), ('d', 3)]
END BFS

DFS
Input graph: nodeName (color, [adj list]) dictionary
a ('white', ['b'])
b ('white', ['c'])
c ('white', ['a', 'd'])
d ('white', ['c'])
Root node a
graph with root a is cyclic
END DFS
"""

import sys



def read(filename):
    """
    read file filename into dictionary
    each line has a node_name followed by its adjacent node_names
    """

    graph = {}  # graph represented by dictionary

    with open(filename) as file:
        for line in file:
            line = line.strip().split(" ")

            if line == ['']:  # ignore empty lines
                continue

            # dictionary: color -> adjList of names
            graph[line[0]] = ('white', line[1:])

    return graph


def print_graph(graph):
    """
    prints out the whole graph dictionary
    :param graph: the graph to be printed
    """
    print("Input graph: nodeName (color, [adj list]) dictionary ")
    for e in graph:
        print(e, graph[e])


def paint_white(graph):
    """
     paint all graph nodes white
    """
    for e in graph:
        graph[e] = ('white', graph[e][1])


'''
  return breadth_first_search queue with (node, distance) pairs
'''


def breadth_first_search(graph, root):
    """
    breadth first search the graph from root
    """
    pass


'''
  return boolean: True gr bfrom r is cyclic, False otherwise
'''


def depth_first_search(graph, root):
    """
    depth first search gr from r for cycles
    """
    pass


if __name__ == "__main__":
    print(sys.argv[0])
    graph = read(sys.argv[1])  # file name
    root = sys.argv[2]  # root node
    is_debug = len(sys.argv) > 3  # debug?

    print("BFS")
    print_graph(graph)
    print("Root node:", root)
    graph[root] = ('black', graph[root][1])
    q = breadth_first_search(graph, [(root, 0)])
    print("BFS queue: (node name, distance) pairs")
    print(q)
    print("END BFS")
    print()

    print("DFS")
    paint_white(graph)
    print_graph(graph)
    print("Root node", root)
    cyclic = depth_first_search(graph, root)
    if cyclic:
        print("graph with root", root, "is cyclic")
    else:
        print("graph with root", root, "is not cyclic")
    print("END DFS")

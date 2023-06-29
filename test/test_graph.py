#!/usr/bin/env python3

import sys
sys.path.append("/workspaces/eda/lib")
import graph

g = graph.Graph()

n1 = graph.Node()
n2 = graph.Node()
n3 = graph.Node()

e1 = graph.Edge([n1,n2])
e2 = graph.Edge([n2,n3])

g.add_node(n1)
g.add_node(n2)
g.add_node(n3)

g.add_edge(e1)
g.add_edge(e2)



g.dump()
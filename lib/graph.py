"""
This module implements Classes and Methods for Graph creation and manipulation 
"""

class Node:
    """ Node of a graph is where edges meet """
    edges = []
    def __init__(self, name: str):
        self.name = name

class Edge:
    """ Connection between two nodes """
    def __init__(self, name: str, nodes: tuple):
        self.name = name
        self.nodes = nodes

class Graph:
    """ A network of nodes and edges """
    nodes = set() # Set of all nodes in the graph
    edges = set() # Set of all edges in the graph
    def __init__(self, name: str):
        self.name = name
    def add_node(self,node: Node):
        """ Add a node to the graph """
        self.nodes.add(node)
        for edge in node.edges:
            if not edge in self.edges:
                self.add_edge(edge)
    def remove_node(self, node: Node):
        """ Removing a node from the graph """
        # Remove all the edges connected to that node
        for edge in node.edges:
            if edge in self.edges:
                self.edges.remove(edge)
        # Remove the node itself
        self.nodes.remove(node)
    def add_edge(self,edge: Node):
        """ Add an edge to the graph """
        self.edges.add(edge)
        for node in edge.nodes:
            if not node in self.nodes:
                self.add_node(node)
    def remove_edge(self, edge: Edge):
        """ Removing an edge from the graph """
        self.edges.remove(edge)

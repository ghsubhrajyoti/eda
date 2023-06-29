"""
This module implements Classes and Methods for Graph creation and manipulation 
"""

class Node:
    """ node of a graph is where edges meet """
    def __init__(self):
        self.edges = set()
    def remove(self):
        """ remove itself and its connected edges """
        for edge in self.edges:
            edge.remove()

class Edge:
    """ connection between two nodes """
    def __init__(self, nodes: list):
        self.nodes = set()
        for node in nodes:
            self.nodes.add(node)
            if not self in node.edges:
                node.edges.add(self)
    def remove(self):
        """ remove itself """
        for node in self.nodes:
            if self in node.edges:
                node.edges.remove(self)
        self.nodes = set()

class Graph:
    """ a network of nodes and edges """
    def __init__(self):
        self.nodes = set() # Set of all nodes in the graph
        self.edges = set() # Set of all edges in the graph
    def add_node(self,node: Node):
        """ add a node to the graph """
        self.nodes.add(node)
    def remove_node(self, node: Node):
        """ removing a node from the graph """
        node.remove()
        self.nodes.remove(node)
    def add_edge(self,edge: Node):
        """ add an edge to the graph """
        self.edges.add(edge)
    def remove_edge(self, edge: Edge):
        """ removing an edge from the graph """
        edge.remove()
        self.edges.remove(edge)
    def dump(self):
        """ print graph as netlist using pseudonames """
        edge_list = []
        node_list = []
        for edge in self.edges:
            if not edge in edge_list:
                edge_list.append(edge)
            line = f"e{edge_list.index(edge)}"
            for node in edge.nodes:
                if not node in node_list:
                    node_list.append(node)
                line += f" n{node_list.index(node)}"
            print(line)
            
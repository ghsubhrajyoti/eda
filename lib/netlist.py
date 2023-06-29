"""
This module contains classes and methods related to circuit netlist
"""

import graph

#=================
# PARENT CLASSES
#=================

class Node(graph.Node):
    """ Termianls of electronic devices """
    def __init__(self, name: str):
        self.name = name
        super().__init__()

class Device(graph.Edge):
    """ Electronic circuit devices """
    def __init__(self,  device_name: str, terminal_names: tuple, nodes: tuple):
        self.device_name = device_name
        self.terminal_names = terminal_names
        self.terminals = nodes
        super().__init__(nodes)

class Netlist(graph.Graph):
    """ Netlist """
    def __init__(self, name: str):
        self.name = name
        super().__init__()

#=====================
# DEVICE DEFINITIONS
#=====================

class Resistor(Device):
    """ Two terminal resistor device """
    __device_name = "resistor"
    __terminal_names = ("plus", "minus")
    def __init__(self, instance_name: str, plus: Node, minus: Node):
        self.instance_name = instance_name
        self.plus = plus
        self.minus = minus
        super().__init__(self.__device_name, self.__terminal_names, (self.plus, self.minus))

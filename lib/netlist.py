"""
This module contains classes and methods related to circuit netlist
"""

import graph

# ================
# PARENT CLASSES
# ================


class Node(graph.Node):
    """ Terminals of electronic devices """
    def __init__(self, name: str):
        self.name = name
        super().__init__()


class Device(graph.Edge):
    """ Electronic circuit devices """
    def __init__(self,  device_name: str, terminal_names: tuple, nodes: tuple):
        self.device_name = device_name
        self.terminal_names = terminal_names
        self.terminals = nodes
        super().__init__(list(nodes))


class Netlist(graph.Graph):
    """ Netlist """
    def __init__(self, name: str):
        self.name = name
        super().__init__()

    def add_device(self, device: Device):
        self.add_edge(device)

# ====================
# DEVICE DEFINITIONS
# ====================


class Resistor(Device):
    """ Two terminal resistor device """
    __device_name = "resistor"
    __terminal_names = ("plus", "minus")

    def __init__(self, instance_name: str, plus: Node, minus: Node):
        self.instance_name = instance_name
        self.plus = plus
        self.minus = minus
        super().__init__(self.__device_name, self.__terminal_names, (self.plus, self.minus))


class DesignResistor(Device):
    """ Three terminal design resistor device """
    __device_name = "design_resistor"
    __terminal_names = ("plus", "minus", "body")

    def __init__(self, instance_name: str, plus: Node, minus: Node, body: Node):
        self.instance_name = instance_name
        self.plus = plus
        self.minus = minus
        self.body = body
        super().__init__(self.__device_name, self.__terminal_names, (self.plus, self.minus, self.body))


class NMOS(Device):
    """ Three terminal n-type mosfet device """
    __device_name = "nmos"
    __terminal_names = ("plus", "minus", "body")

    def __init__(self, instance_name: str, plus: Node, minus: Node, body: Node):
        self.instance_name = instance_name
        self.plus = plus
        self.minus = minus
        self.body = body
        super().__init__(self.__device_name, self.__terminal_names, (self.plus, self.minus, self.body))


class PMOS(Device):
    """ Four terminal p-type mosfet device """
    __device_name = "nmos"
    __terminal_names = ("plus", "minus", "body", "substrate")

    def __init__(self, instance_name: str, plus: Node, minus: Node, body: Node, substrate: Node):
        self.instance_name = instance_name
        self.plus = plus
        self.minus = minus
        self.body = body
        self.substrate = substrate
        super().__init__(self.__device_name, self.__terminal_names, (self.plus, self.minus, self.body, self.substrate))

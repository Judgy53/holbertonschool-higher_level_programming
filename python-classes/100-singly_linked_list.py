#!/usr/bin/python3
"""Defines a Singly linked List and its nodes"""


class Node():
    """Represents a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize this instance with data and link to next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property Getter of data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Property Setter of data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Property Getter of next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property Setter of next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Represents a list of singly linked nodes"""

    def __init__(self):
        """Initialize the list"""
        self.__head = None

    def __str__(self):
        """Returns the entire list, one node per line"""
        if self.__head is None:
            return ""
        out = ""
        node = self.__head
        while node is not None:
            out += "{}\n".format(str(node.data))
            node = node.next_node
        return out[:-1]

    def sorted_insert(self, value):
        """Inserts a new value in the sorted list"""
        if self.__head is None:
            self.__head = Node(value)
            return

        node = self.__head
        while True:
            if value < node.data:
                tmp = node.data
                node.data = value
                value = tmp
            if node.next_node is None:
                node.next_node = Node(value)
                return
            node = node.next_node

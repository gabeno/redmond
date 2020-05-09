class Node:
    """Node in a linked list

    Node has two components:

        - data: value to be stored
        - pointer: refers to the next node
    """
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    """Linked List

    Sample representation:

        head_node -> Node -> Node -> ... -> None
    """
    def __init__(self, node):
        self.head_node = node

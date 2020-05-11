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

    def get_head(self):
        """returns the head of the list"""
        return self.head_node

    def is_empty(self):
        """returns true if the linked list is empty"""
        return self.head_node is None
    def __repr__(self):
        """Helper method for visually seeing our linked list"""
        if (self.is_empty()):
            return f"{self.__class__.__name__} is empty"

        temp = self.head_node
        s = ""
        while temp.next_element is not None:
            s += f"{temp.data} -> "
            temp = temp.next_element
        s += f"{temp.data} -> None"
        return s

if __name__ == "__main__":
    l = LinkedList(None)
    print(l)

    l = LinkedList(Node("1"))
    print(l)

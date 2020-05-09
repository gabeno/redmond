import pytest

from modules.linked_list import LinkedList, Node


class TestLinkedList:
    def test__initialize__is_empty(self):
        first_node = Node("fake data")
        assert first_node.data == "fake data"
        assert first_node.next_element is None

        alist = LinkedList(first_node)
        assert alist.head_node == first_node

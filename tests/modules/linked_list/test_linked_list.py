import pytest

from modules.linked_list import LinkedList, Node


class TestLinkedList:
    def test__initialize__is_empty(self):
        first_node = Node("fake data")
        assert first_node.data == "fake data"
        assert first_node.next_element is None

        alist = LinkedList(first_node)
        assert alist.head_node == first_node

    def test__get_head_node__ok(self):
        node = Node("a")
        alist = LinkedList(node)
        assert alist.get_head() == node

    def test__is_empty__ok(self):
        alist = LinkedList(None)
        node = Node("a")
        blist = LinkedList(node)
        assert alist.is_empty() is True
        assert blist.is_empty() is False

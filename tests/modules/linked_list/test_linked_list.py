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
        alist = LinkedList()
        node = Node("a")
        blist = LinkedList(node)
        assert alist.is_empty() is True
        assert blist.is_empty() is False

    def test_list_empty__insert_at_head__ok(self):
        alist = LinkedList()
        assert alist.is_empty() is True
        assert alist.get_head() is None
        data = 1
        alist.insert_at_head(data)
        assert alist.is_empty() is False
        assert alist.get_head().data == data
        assert str(alist) == f"{data} -> None"

    def test_list_not_empty__insert_at_head__ok(self):
        alist = LinkedList(Node("1"))
        assert alist.is_empty() is False
        assert alist.get_head() is not None
        data = 2
        alist.insert_at_head(data)
        assert alist.is_empty() is False
        assert alist.get_head().data == data
        assert str(alist) == f"{data} -> 1 -> None"

    def test_list_empty__insert_at_tail__ok(self):
        alist = LinkedList()
        assert alist.is_empty() is True
        assert alist.get_head() is None
        data = 1
        alist.insert_at_tail(data)
        assert alist.is_empty() is False
        assert alist.get_head().data == data
        assert str(alist) == f"{data} -> None"

    def test_list_not_empty__insert_at_tail__ok(self):
        alist = LinkedList(Node("1"))
        assert alist.is_empty() is False
        assert alist.get_head() is not None
        data = 2
        alist.insert_at_tail(data)
        assert alist.is_empty() is False
        assert str(alist) == f"1 -> {data} -> None"
        data = 3
        alist.insert_at_tail(data)
        assert alist.is_empty() is False
        assert str(alist) == f"1 -> 2 -> {data} -> None"

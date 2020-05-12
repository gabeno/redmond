import pytest

from modules.linked_list import LinkedList, Node


class TestLinkedList:
    def test_init__with_node__ok(self):
        first_node = Node("fake data")
        assert first_node.data == "fake data"
        assert first_node.next_element is None

        alist = LinkedList(first_node)
        assert alist.head_node == first_node

    def test_get_head__ok(self):
        node = Node("a")
        alist = LinkedList(node)
        assert alist.get_head() == node

    def test_is_empty__empty_list__ok(self):
        alist = LinkedList()
        node = Node("a")
        blist = LinkedList(node)
        assert alist.is_empty() is True
        assert blist.is_empty() is False

    def test_insert_at_head__empty_list__ok(self):
        alist = LinkedList()
        assert alist.is_empty() is True
        assert alist.get_head() is None
        data = 1
        alist.insert_at_head(data)
        assert alist.is_empty() is False
        assert alist.get_head().data == data
        assert str(alist) == f"{data} -> None"

    def test_insert_at_head__non_empty_list__ok(self):
        alist = LinkedList(Node("1"))
        assert alist.is_empty() is False
        assert alist.get_head() is not None
        data = 2
        alist.insert_at_head(data)
        assert alist.is_empty() is False
        assert alist.get_head().data == data
        assert str(alist) == f"{data} -> 1 -> None"

    def test_insert_at_tail__empty_list__ok(self):
        alist = LinkedList()
        assert alist.is_empty() is True
        assert alist.get_head() is None
        data = 1
        alist.insert_at_tail(data)
        assert alist.is_empty() is False
        assert alist.get_head().data == data
        assert str(alist) == f"{data} -> None"

    def test_insert_at_tail__non_empty_list__ok(self):
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

    def test_insert_at_position__empty_list_position_one__ok(self):
        alist = LinkedList()
        data, position = 1, 0
        alist.insert_at_position(data, position)
        assert alist.is_empty() is False
        assert alist.get_head().data == data
        assert str(alist) == f"{data} -> None"

    def test_insert_at_position__empty_list_position_greater_than_one__ok(self):
        alist = LinkedList()
        data, position = 1, 5
        alist.insert_at_position(data, position)
        assert alist.is_empty() is False
        assert alist.get_head().data == data
        assert str(alist) == f"{data} -> None"

    def test_insert_at_position__position_equals_head__ok(self):
        alist = LinkedList()
        for i in range(1, 4):
            alist.insert_at_head(i)
        assert str(alist) == "3 -> 2 -> 1 -> None"
        data, position = "xxx", 0
        alist.insert_at_position(data, position)
        assert alist.get_head().data == data
        assert str(alist) == f"xxx -> 3 -> 2 -> 1 -> None"

    def test_insert_at_position__position_equals_tail__ok(self):
        alist = LinkedList()
        for i in range(1, 4):
            alist.insert_at_head(i)
        assert str(alist) == "3 -> 2 -> 1 -> None"
        data, position = "xxx", 2
        alist.insert_at_position(data, position)
        assert str(alist) == f"3 -> 2 -> 1 -> xxx -> None"

    def test_insert_at_position__position_middle__ok(self):
        alist = LinkedList()
        for i in range(1, 4):
            alist.insert_at_head(i)
        assert str(alist) == "3 -> 2 -> 1 -> None"
        data, position = "xxx", 1
        alist.insert_at_position(data, position)
        assert str(alist) == f"3 -> xxx -> 2 -> 1 -> None"

    def test_insert_at_position__negative_position__raises(self):
        with pytest.raises(Exception):
            alist = LinkedList()
            for i in range(1, 4):
                alist.insert_at_head(i)
            assert str(alist) == "3 -> 2 -> 1 -> None"
            alist.insert_at_position("xxx", -1)

    def test_insert_at_position__position_out_of_range__raises(self):
        with pytest.raises(Exception):
            alist = LinkedList()
            for i in range(1, 4):
                alist.insert_at_head(i)
            assert str(alist) == "3 -> 2 -> 1 -> None"
            alist.insert_at_position("xxx", 3)

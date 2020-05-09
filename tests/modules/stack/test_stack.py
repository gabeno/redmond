import pytest

from modules.stack import Stack


class TestStackADT(object):
    def test__new_stack__is_empty(self):
        s = Stack()
        assert s.size() == 0
        assert s.is_empty() == True
        assert s.peek() == None

    def test__stack_operations__ok(self):
        s = Stack()
        s.push(10)
        assert s.size() == 1
        assert s.peek() == 10
        s.push(22)
        assert s.size() == 2
        assert s.peek() == 22
        assert s.is_empty() == False
        s.pop()
        assert s.size() == 1
        s.pop()
        assert s.size() == 0
        assert s.is_empty() == True

    def test__pop_empty_stack__raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.pop()

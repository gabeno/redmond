class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        """
        Remove the top element from the stack

        return element
        """
        try:
            return self.stack.pop()
        except IndexError:
            raise

    def peek(self):
        """
        Return the top element
        """
        elem = None
        if self.size() > 0:
            elem = self.stack[self.size() - 1]
        return elem

    def size(self):
        """
        Number of elements in a stack
        """
        return len(self.stack)

    def is_empty(self):
        """Return False when stack has elements"""
        return self.size() == 0

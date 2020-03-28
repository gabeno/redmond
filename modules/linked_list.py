class Node:
    """Node holds data of type integer"""

    def __init__(self, data=0):
        self.data = data
        self.next_node = None


class LinkedList:
    """Linked list implementation"""

    def __init__(self):
        self.head = None

    def get_head(self):
        """Get head node

        An empty linked list has a head node pointing to None
        time = O(1) => get head
        """
        return self.head

    def is_empty(self):
        """Check if node is empty

        An empty linked list has only head node
        time = O(1) => check whether head points to None or another node
        """
        return self.head is None

    def insert_at_head(self, data):
        """Insert an element at the head on the node

        time = O(1) => point the head to a new node each time
        """
        temp = Node(data)
        temp.next_node = self.head
        self.head = temp
        return self.head

    def insert_at_tail(self, data):
        """Insert data at end of the list

        time = O(n) => traverses the whole list
        """
        head = self.get_head()

        if head is None:
            self.insert_at_head(data)
            return

        while head.next_node:
            head = head.next_node

        head.next_node = Node(data)
        return

    def insert_at_position(self, data, pos):
        """Insert data at a position in the list

        """
        assert pos > 0
        current_head = self.get_head()
        i = 1
        prev_head = None

        if self.is_empty() or pos ==1:
            self.insert_at_head(data)
            return

        while current_head.next_node:
            if pos == i:
                temp = Node(data)
                prev_head.next_node = temp
                temp.next_node = current_head
            prev_head, current_head = current_head, current_head.next_node
            i += 1

        # we could :
        # - fail and note that pos is out of range
        # - insert at the end of the list
        if pos >= i:
            raise Exception(f"position {pos} is out of range")
            # self.insert_at_tail(data)

    def print_list(self):
        if self.is_empty():
            print("List is empty")
        else:
            temp = self.head
            while temp.next_node is not None:
                print(temp.data, end=" -> ")
                temp = temp.next_node
            print(temp.data, end=" -> None")
            print()
            return True


if __name__ == "__main__":
    L = LinkedList()
    print(L.is_empty())
    L.print_list()

    print(f"Inserting {5} elements")
    for i in range(1, 5):
        L.insert_at_head(i)
    L.print_list()
    L.insert_at_tail(10)
    L.print_list()

    L.insert_at_position(23, 6)
    L.print_list()

    #L2 = LinkedList()
    #L2.insert_at_tail(10)
    #L2.print_list()

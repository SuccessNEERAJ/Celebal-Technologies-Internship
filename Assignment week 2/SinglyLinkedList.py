class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Manages a singly linked list."""
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        """Add a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print all the nodes in the list."""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index) from the list."""
        if not self.head:
            raise IndexError("Cannot delete from an empty list.")

        if n <= 0:
            raise ValueError("Index must be a positive integer.")

        if n == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            print(f"Deleted node with data: {deleted_data}")
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError(f"Index {n} is out of range.")

        prev.next = current.next
        print(f"Deleted node with data: {current.data}")


# Test the LinkedList
if __name__ == "__main__":
    ll = LinkedList()

    # Add nodes to the list
    ll.add_to_end(10)
    ll.add_to_end(20)
    ll.add_to_end(30)
    ll.add_to_end(40)

    # Print the list
    ll.print_list()

    # Delete 2nd node
    ll.delete_nth_node(2)
    ll.print_list()

    # Delete 1st node
    ll.delete_nth_node(1)
    ll.print_list()

    # Try deleting a node with an out-of-range index
    try:
        ll.delete_nth_node(10)
    except IndexError as e:
        print("Error:", e)

    # Try deleting from an empty list
    try:
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)
    except IndexError as e:
        print("Error:", e)

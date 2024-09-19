class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

# Test case
def test_reverse_linked_list():
    linked_list = SinglyLinkedList()
    
    # Appending elements to the linked list
    for i in [1, 2, 3, 4, 5]:
        linked_list.append(i)
    
    # Original linked list: [1, 2, 3, 4, 5]
    assert linked_list.display() == [1, 2, 3, 4, 5]
    
    # Reverse the linked list
    linked_list.reverse()
    
    # After reversing, the linked list should be: [5, 4, 3, 2, 1]
    assert linked_list.display() == [5, 4, 3, 2, 1]
    
    print("All test cases passed!")

# Running the test case
test_reverse_linked_list()

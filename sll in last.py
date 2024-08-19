class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    
    # Inserting elements at the end
    linked_list.insert_at_last(10)
    linked_list.insert_at_last(20)
    linked_list.insert_at_last(30)
    
    # Printing the linked list
    linked_list.print_list()

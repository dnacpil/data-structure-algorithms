""" 
Linked List Operations:
Implement a Python class for a singly linked list. Include methods to:
Insert a node at the beginning/end of the list.
Delete a node by value.
Search for a node by value.
Print the linked list. 
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Sample usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(15)
    linked_list.insert_at_beginning(2)
    
    print("Linked List:")
    linked_list.print_list()  # Output: 2 5 10 15
    
    linked_list.delete_node(10)
    print("Linked List after deleting 10:")
    linked_list.print_list()  # Output: 2 5 15
    
    print("Search for 5:", linked_list.search(5))  # Output: True
    print("Search for 20:", linked_list.search(20))  # Output: False

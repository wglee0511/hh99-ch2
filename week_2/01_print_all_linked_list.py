
from typing import Counter


class Node : 
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self, data) :
        self.head = Node(data)
        
    def append(self, data):
        if self.head is None :
            self.head = Node(data)
            return
        current_value = self.head
        while current_value.next is not None :
            current_value = current_value.next
        current_value.next = Node(data)

    def print_all(self):
        current_value = self.head
        while current_value is not None :
            print(current_value.data)
            current_value = current_value.next

linked_list = LinkedList(3)
linked_list.append(6)
linked_list.append(10)
linked_list.print_all()
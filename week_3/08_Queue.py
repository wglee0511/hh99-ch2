class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 어떻게 하면 될까요?
        new_node = Node(value)
        if self.is_empty() :
            self.head =new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

        return

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        # 어떻게 하면 될까요?
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.head.data

    def is_empty(self):
        return self.head is None
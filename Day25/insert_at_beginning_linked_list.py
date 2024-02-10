class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_end(self, data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node

    def insert_at_beginning(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def print(self):
        current_node=self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node=current_node.next
        print("Null")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)

    linked_list.print()

    linked_list.insert_at_beginning(0)

    linked_list.print()

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

    def delete_last_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        second_last=self.head
        while second_last.next.next:
            second_last=second_last.next
        second_last.next=None

    def print(self):
        current_node=self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node=current_node.next
        print("Null")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(12)
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(8)
    linked_list.insert_at_end(7)

    linked_list.print()

    linked_list.delete_last_node()

    linked_list.print()

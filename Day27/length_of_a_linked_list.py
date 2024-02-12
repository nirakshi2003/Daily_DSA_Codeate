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

    def length(self):
        current=self.head
        length=0
        while current:
            length+=1
            current=current.next
        return length

    def print(self):
        current_node=self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node=current_node.next
        print("Null")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(8)
    linked_list.insert_at_end(7)

    linked_list.print()

    print("Length if the Linked List :", linked_list.length())

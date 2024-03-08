#contains two pointers prev and next
'''
One pointer is for the previous node and other for the next node
here we can traverse in both the directions unlike singly linked list where we traverse only in one direction
Head will obviously be pointing at the first node
'''
class Node:
    def __init__(self,data):
        self.data =data
        self.next =None #initally no next and no prev which is obvious
        self.prev =None

class DoublyLL:
    def __init__(self):
        self.head =None

    def forward_traversal(self):
        print()
        if self.head is None:
            print("Linked List is empty")

        else:
            a=self.head
            while a is not None:#until the end vanna khojya ho
                print(a.data,end=" ")
                a =a.next

    def backward_traversal(self):
        print()
        if self.head is None:
            print("Lineked list is empty")

        else:
            a =self.head
            while a.next is not None:#traverses to the last and makes the last node head
                a=a.next
            while a is not None:
                print(a.data,end=" ")#not from the last we backward traverse
                a=a.prev #with this               

n1=Node(10)
dll = DoublyLL()
dll.head = n1
n2= Node(20)
n2.prev =n1
n1.next = n2
n3=Node(30)
n3.prev =n2
n2.next = n3
n4=Node(40)
n4.prev = n3
n3.next =n4
dll.forward_traversal()
dll.backward_traversal()

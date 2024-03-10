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
                print(a.data,end=" ")#now from the last we backward traverse
                a=a.prev #with this               


    def insert_at_beginning(self,data):
        ns = Node(data)
        a = self.head
        a.prev =ns
        ns.next = a
        self.head = ns

    def insert_at_end(self,data):
        ne = Node(data)
        a= self.head
        while a.next is not None:
            a = a.next
        a.next = ne
        ne.prev = a

    def insert_at_specified_node(self,data,position):
        nib = Node(data)
        a=self.head
        for i in range(1, position-1):
            a=a.next  

        nib.prev = a
        nib.next = a.next
        a.next.prev = nib
        a.next = nib 

    def delete_at_beginning(self) :
        a=self.head
        self.head = a.next
        a.next = None
        self.head.prev = None

    def delete_at_end(self):
        a = self.head.next
        before = self.head
        while a.next is not None:
            a=a.next# one running a step ahead than the other
            before = before.next #this is one step behind
        before.next =None #agadi ko gayera nali ma khasyo but you dont go
        a.prev =None   # the one infront disconnects too

    def delete_at_specified_node(self,position):
        a = self.head.next
        before = self.head
        for i in range(1,position-1):
            a=a.next
            before=before.next

        before.next = a.next
        a.next.prev = before # banauni sambanda paila bana tespaxi balla todni sambanda tod, like playing it safe, euta kaam xodni vanda paila euta khojisakera todni
        a.next = None
        a.prev = None
                     



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
dll.insert_at_specified_node(5,2)
dll.delete_at_beginning()
dll.delete_at_end()
dll.delete_at_specified_node(2)
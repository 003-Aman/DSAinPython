#insert,delete,traversal and get length in linked list
# basically a linked list has a data which is the value it stores like 1,A,Aman or whatever but a value
#it has a pointer named next which points to the value of the next node or upcoming node
#head points to the first node(not the data of the first node) and tail points to the last node

class Node:
    def __init__(self,data):
        self.data = data #node banayo vane data ta hunai paryo natra k ko node
        self.next = None # tara this node doesnt point to anything , this is just an individual node not a linked list

class LinkedList:
    def __init__(self):
        self.head = None # we created a linked which has no items as if now so no head and no value to point at

    def insertAtBegin(self,data):#shuru ma halni ra value pani chaiyo data ko jun halni ho
        new_node = Node(data) #insert at beginning garda pani euta value ta dinai paryo which we do by creating a node a  node is value and pointer next
        if self.head == None: # insert at beginning garda node empty nai huna parxa vane xaina so we are checking
            self.head = new_node
            return 
        else:
            new_node.next = self.head
            self.head = new_node #updating the head value paxadi link todera agadi ayera joddiyo

    def insertAtIndex(self,data,index):
        new_node = Node(data)# makes a new node when you call the function
        current_node = self.head #current_node refers to the head of the linked list
        position =0 #these variables are used to traverse the linked list and keep track of the current position
        if position == index: #if the provided index is 0 it means that we want to insert at the beginning of the linked list
            self.insertAtBegin(data)
        else:
            while current_node!=None and position+1 !=index: #traverses the linked list until either current_node becomes None(indicating the end of the list) or position +1 equals to the specified index
                position = position +1 #with each iteration, it increments the position and moves current_node to the next node
                current_node = current_node.next

            if current_node != None: #checks if the specified index is valid and there's a node at that position
                new_node.next = current_node.next #If so, it inserts a new node between current_node and its next node
                current_node.next = new_node #by updating the 'next' pointers accordingly
            else:
                print("Index not present") #if current node is None after traversing the linked list, it means the specified index is beyond the end of the list 


    def insertAtEnd(self,data):
        new_node = Node(data)# j garda pani node ta banauna paryo kinabhane here the value is a node jastai ho which has next too
        if self.head == None: #this checks if the linkedlist has no items
            self.head = new_node # if it is, point the head to the new node which we have created
            return 

        current_node = self.head #yo else ho, make a variable current_node and make it the self.head
        while current_node.next: #self.head.next
            current_node =current_node.next # agadi ko ma point gara
        current_node.next = new_node   #agadi aba new node jodde 

    def updateNode(self,val,index): #update the value of a node at a given index
        current_node =self.head
        position =0
        if position ==index: #which means that if index is 0
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position +1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index is not present") 

    def remove_first_node(self):
        if self.head == None:#which means no node
            return 
        self.head = self.head.next # passing the head pointer to the one infront

    def remove_last_node(self):
        if self.head is None:
            return 
        current_node = self.head #else

        while current_node.next.next:
            current_node=current_node.next 

        current_node.next =None

    def remove_at_index(self,index):
        if self.head == None:
            return

        current_node =self.head
        position =0
        if position ==index:
            self.remove_first_node()

        else:
            while current_node != None and position +1 != index:
                position = position +1
                current_node= current_node.next

            if current_node != None:
                current_node.next = current_node.next.next

            else:
                print("Index not present")   

    def remove_node(self,data):
        current_node = self.head

        if current_node.data ==data:
            self.remove_first_node() 
            return

        while current_node != None and current_node.next.data != data:
            current_node = current_node.next

        if current_node == None: 
            return
        else:
            current_node.next = current_node.next.next

    def sizeOfLL(self):
        size =0
        if self.head:
            current_node = self.head
            while(current_node):
                size = size +1
                current_node = current_node.next

            return size

        else:
            return 0

    def printLL(self):
        current_node =self.head
        while current_node:
            print(current_node.data)
            current_node=current_node.next


llist = LinkedList()
llist.insertAtEnd("Aman")
llist.insertAtEnd("Piyush")
llist.insertAtBegin("Bidya")
llist.insertAtBegin("Kumar")
llist.insertAtIndex("Sushil",2)

print("Node data")
llist.printLL()

print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)
 
 
# print the linked list again
print("\nLinked list after removing a node:")
llist.printLL()
 
print("\nUpdate node Value")
llist.updateNode('Pramod', 0)
llist.printLL()
 
print("\nSize of linked list :", end=" ")
print(llist.sizeOfLL())

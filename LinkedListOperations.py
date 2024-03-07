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
        if self.head == None:
            self.head = new_node
            return 

        current_node = self.head 
        while current_node.next:
            current_node =current_node.next
        current_node.next = new_node    

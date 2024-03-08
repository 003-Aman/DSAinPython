'''
Collection of a group of nodes
each node contains data and reference(pointer) which contains the address of next node
eg.Head-->['Aman',2020]->['Piyush',2030]->['Pramod',  ]-->Null
             N1=2010         N2=2020         N3=2030
N1,N2 and N3 are addresses of the nodes and they have data and reference
reference is basically the address of the next node
             
'''
#accessing the elements will be slower compared to list because linked list needs a traversal
#utlization of memory will be more compared to list



#Creating a node
class Node:
    def __init__(self,data):
        self.data = data #n1.data =5,n2.data=10 and so on intially
        self.next = None #n1.next = None,so on, n4.next = None initially

n1=Node(8)
print(n1.data) 
print(n1.next)

#creating a class of Singly Linked list
class SinglyLL:
    def __init__(self):#whenever you create an object whatever is inside the init constructor will execute
        self.head = None

#TRAVERSAL IN LINKED LIST
    def traversal(self): 
        if self.head is None:
            print("Singly linked list is empty.") 
        else:
            a=self.head #a =sll.head
            #we can do a traversal only when there are items
            # creating a variable to store the value of head so that it doesnt change
            while a is not None: #a=sll.head
                print(a.data, end=" ") #a.data=n1.data, n2.data
                #keep printing the data
                a = a.next #a =n1.next,n2.next
                  #transfer the value of a to the next a and run the while loop again 
                
    def insert_at_beginning(self,data): #data =2
        print()
        nb = Node(data) #nb=Node(2)
        nb.next = self.head #the next of the new node is connected to where the head is pointing now
        self.head = nb #now connect the previous head to the new node


    def insert_at_end(self,data):
        print() #to get space between the outputs
        ne = Node(data)
        #we are creating a temporary variable because we will have to use a while loop and the value of the head doesnt change 
        a=self.head #a =sll.head =nb
        while a.next is not None: #traverse and pass the value until it reaches the last and a.next becomes None
            a=a.next #loop will end at n4.next = None
        a.next =ne #after the while loop is ended make the last node next point to the new node ne n4.next =ne 


    def insert_at_specified_node(self,data,position):
        print()
        nib = Node(data)
        a=self.head
        for i in range(1,position-1):#specified index ko agadi samma iterate
            a=a.next
        nib.next = a.next #point to the same node both
        a.next =nib #pull out the previous node and point to the new


    def deletion_at_beginning(self):
        print() #no need to create a new node obviously
        a=self.head #visualize that both a and self.head are pointing to the first node
        self.head = a.next #we move the self.head and make it point to the second node
        a.next = None #a is also pointing to the first node and we make a.next None which means that it does have the address of the upcoming node now
        #which means it got disconnected but self.head moved so the node was deleted at the beginning


    def deletion_at_end(self): #you have to go through each node through each node you cant directly jump to the last one in linkedlist
        print()
        prev =self.head #initial node lai elle point garaideko yo bela prev le
        a=self.head.next # ani aile a lai chai agadi ko lai second node
        while a.next is not None: #so basically self.head.next.next
            #this is checking 1 kadam agadi khali xaina vane
            a=a.next #agadi bada
            prev = prev.next #yo pani agadi badhdai xa tara a vanda 1 kadam paxadi xa
        prev.next = None #the while loop ends then list is over and a.next is None
        #so come out of the while loop and dont go forward disconnect   

    def deletion_at_specified_node(self,position):
        print()
        prev=self.head
        a=self.head.next
        for i in range(1,position): #this time a doesnt stop before it reaches the position but reaches there
            a=a.next
            prev =prev.next
        
        prev.next = a.next #when a reaches there we make the prev.next equal to the a.next directly, we skip and node and connect to the alternate one directly
        a.next = None  # and disconnect the a.next from the next since prev.next maintained the connection 


sll=SinglyLL()  #sll.head =None

n1=Node(5)
sll.head =n1 #sll.head =n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next =n3
n4=Node(20)
n3.next =n4
sll.traversal()
sll.insert_at_beginning(2)
sll.traversal()
sll.insert_at_end(25)
sll.traversal()
sll.insert_at_specified_node(12,3)
sll.traversal()
sll.deletion_at_beginning()
sll.traversal()
sll.deletion_at_end()
sll.traversal()
sll.deletion_at_specified_node(1) #1 means the second element like indexing
sll.traversal()







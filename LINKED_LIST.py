'''
linked list is like treasure hunt where each clue includes the information about the next clue

Linked List Applications
image viewer
previous and next page in web browser
music player
gps navigation
robotics
task scheduling, image processing
Dynamic memory allocation
Implemented in stack and queue
In undo functionality of softwares
Hash tables, Graphs
'''
#simple linked list using python
class Node:# represents a single node in the linked list
    def __init__(self,item):# object banauni bela you need to pass an arguement which will be the value that the node holds
        self.item =item #this assigns the value of the node to the item attribute
        self.next = None # initially there is no next node connected to this node

class LinkedList:
    def __init__(self):# naya linked list banauxa with no nodes
        self.head = None # head to None which means initial object banauda there is no element and is empty

if __name__=="__main__":# this checks if the script is being run directly as the main program
    linked_list = LinkedList() #object named linked_list is created using Linkedlist class

    #Assign item values
    linked_list.head = Node(1) #created the first node passing value of item '1' and assigned it to the value of the head of the linkedlist by updating it's attribute variable
    second = Node(2) #two nodes are created using the node class with object name second and third
    third =Node(3) 
    fourth = Node(7)
    fifth = Node(8)
    sixth = Node(9)

    linked_list.head.next =second # yo vaneko Node(1) which is linked_list.head is connected to the second node y updating or setting next attribute to second
    second.next = third  #third and second connected tesari nai
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth



    while linked_list.head != None: # this line will run as long as the head of the linkedlist is not None which means the linkedlist is not empty
        print(linked_list.head.item, end ="")#This line prints the value of the current node (linked_list.head.item) without moving to the next node in the list
        linked_list.head = linked_list.head.next  #This line updates the head of the linked list to point to the next node, effectively moving to the next node in the list.          
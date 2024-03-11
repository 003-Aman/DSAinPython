class Node:
    def __init__(self,data):
        self.data =data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self,data):#insert at beginning
        new_node = Node(data) 
        cur = self.head # so this is 'a' that we made las time
        new_node.next = self.head 


        if not self.head :#new_node.next nai xaina vane no self.head
            new_node.next = new_node #farkera its pointing to the same node since its circular


        else:  
            while cur.next != self.head:
                cur = cur.next # this is basically traversing unitl it points to self.head since circular
            cur.next = new_node #last samma pugyo until the last node doesnt point to self.heada and tya gayera haldyo node
        self.head = new_node # while visualizing this seems like last ma halyo but from the back it came to the front and became the self.head


    def append(self,data):#insert at the last
        if not self.head:# which means that the linkedlist doesnt have any node not even one
            self.head = Node(data) #then make a node and make it self.head, this is a smart move
            self.head.next = self.head # and point it to itself pucchar to nidhar

        else: # if there already is one or more(not empty)
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node# simple nai xa last ma node halyo ani
            new_node.next = self.head  # made its next point at front


    def print_list(self):
        cur = self.head

        while cur:#means if there is a self.head
            print(cur.data) #print data 
            cur = cur.next #go the next
            if cur == self.head # means cur = cur.next if equals to self.head which means it reached last 
            break   # now break                             



cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()        
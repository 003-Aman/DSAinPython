class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):#push nai raixa last ma
    newP = Node(data)
    newP.next = head

    if head != None:#head is newP.next right now so if there is only one item there can be no next, which is None
        temp = head #like we gave a variable for head we are giving a name here called temp
        while temp.next != head:
            temp = temp.next
        temp.next = newP
    else:
        newP.next = newP#natra ghumerai aayo arko node xaina vane

    head = newP # ani head is new.P
    return head  

def printList(head):
    if head == None:
        print("List is empty")
        return 
    
    temp = head.next # temp lai agadi pathidiyo
    print(head.data, end=' ') # paila yo print garayo
    if head != None: 
        while temp != head: #esto garo chai kina gareko
            print(temp.data, end=" ") # tespaxi aba temp print handai ja sardai
            temp = temp.next #saryo
    print() 
  
def deleteNode(head, key): 
    if head == None: 
        return
  
    if head.data == key and head.next == head: 
        head = None
        return
  
    last = head 
  
    if head.data == key: 
        while last.next != head: 
            last = last.next
  
        last.next = head.next
        head = last.next
        return
  
    while last.next != head and last.next.data != key: 
        last = last.next
  
    if last.next.data == key: 
        d = last.next
        last.next = d.next
        d = None
    else: 
        print("Given node is not found in the list!!!") 

head = None

head = push(head, 2) 
head = push(head, 5) 
head = push(head, 7) 
head = push(head, 8) 
head = push(head, 10) 
  
print("List Before Deletion: ") 
printList(head) 
  
deleteNode(head, 7) 
print("List After Deletion: ") 
printList(head)

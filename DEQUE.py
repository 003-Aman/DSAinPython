#Double Ended Queue
#time complexity for all operations is constant O(1)

#this is a very simple deque using python
#deque means can add and remove from bothh of the sides and neither lifo or fifo works here
class Deque:
    def __init__(self):
        self.items =[]#when we create an object you know it

    def isEmpty(self):
        return self.items ==[] # returns a boolean

    def addRear(self,item): # paxadi add garni
        self.items.append(item)# which can be done by basically append in python
        return self.items # now return the updated deque

    def addFront(self,item):
        self.items.insert(0,item) #insert function can be used
        return self.items     

    def removeFront(self):
        if len(self.items)==0:
            return "Deque is empty"
        self.items.pop(0)

    def removeRear(self):
        if len(self.items)==0:
            return "Deque is empty"
        self.items.pop() 

    def size(self):
        return len(self.items) 

deque = Deque()
print(deque.addFront(2))  
print(deque.addFront(3))  
print(deque.addRear(7))
print(deque.addFront(4))  
print(deque.size())  #done  
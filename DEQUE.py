#Double Ended Queue
#time complexity for all operations is constant O(1)

#this is a very simple deque using python
class Deque:
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items ==[]

    def addRear(self,item):
        self.items.append(item)
        return self.items

    def addFront(self,item):
        self.items.insert(0,item)
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
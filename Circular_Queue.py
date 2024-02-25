class MyCircularQueue:
    def __init__(self,k):
        self.k =k
        self.queue = [None]*k
        self.head = self.tail = -1 # these are the indexices of the rear and front

    def enqueue(self,data):
        if ((self.tail+1)%self.k == self.head):#paxadi full xa ani agadi ko pani 0 index occupied xa vane 
            print("The Circular Queue is full")    

        elif (self.head ==-1): #yo vaneko chai aile samma kei halenaraixa vane
            self.head =0
            self.tail =0 #change both the front and rear indexices to zero which is front ++ and rear ++
            self.queue[self.tail]=data # queue ko tail index ma chai data hal jun ko value ta hami nai dinxam

        else:
            self.tail =(self.tail +1) %self.k #last ko full xa agadi ko khali xa vane
            self.queue[self.tail]=data   #agadi haldine data chai

    def dequeue(self):#esma parameter liyena kinabhane niskini jasari first kai ho FIFO
        if self.head ==-1:
            print("The Queue is empty for deque")

        elif (self.head == self.tail): #euta matrai element raixa vane queue ma
            temp= self.queue[self.head]  #head ma jun element xa tei ta niskinxa
            self.head = -1
            self.tail =-1
            return temp
        
        else: 
            temp=self.queue[self.head]
            self.head =(self.head+1)%self.k #elle chai khasma 1 agadi badxa index kinabhane remainder return garxa try it yourself
            return temp
        
    def printCircularQueue(self):
            if(self.head ==-1):
                print("No element in the circular queue")
        
            elif(self.tail >= self.head ):#euta element matrai vayo vane pani yo condition meet garxa
                for i in range(self.head, self.tail +1):
                    print(self.queue[i], end = " ")   
                print()

            else:
                for i in range(self.head,self.k):
                    print(self.queue[i],end= " ")
                for i in range(0,self.tail +1):
                    print(self.queue[i],end =" ") 
                print()  


obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(3)
obj.enqueue(7)
obj.enqueue(45)
obj.enqueue(27)
print("Initial queue")
obj.printCircularQueue()   
obj.dequeue()
print("After removing an element from the queue")
obj.printCircularQueue()                   
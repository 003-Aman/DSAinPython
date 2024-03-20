'''
Applications of Circular Queue
CPU scheduling
Memory management
Traffic Management
space complexity reduction
repitions in calendar
circular manufacturing machines: bottle cap
'''

class MyCircularQueue:
    def __init__(self,k):
        self.k =k
        self.queue = [None]*k #object banauni bittikai yo value huxa when only parameter k is passed k= no. of items
        self.head = self.tail = -1 # these are the indexices of the rear and front at first when nothing is in the queue

    def enqueue(self,data):#last ma data halna paryo
        if ((self.tail+1)%self.k == self.head):#paxadi full xa ani agadi ko pani 0 index occupied xa vane 
            #suppose 5 xa length of array ani last ko index will be 4 so , 5%5 = 0 , so aba it will go to the first index
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
            temp= self.queue[self.head]  #head ma jun element xa tei ta niskinxa, that value is stored in the temp variable
            self.head = -1#ava tyo euta ni niskiyo so feri duitai -1
            self.tail =-1
            return temp 
        
        else: 
            temp=self.queue[self.head]
            self.head =(self.head+1)%self.k #elle chai khasma 1 agadi badxa index kinabhane remainder return garxa try it yourself
            #so if 2 then 3%5 will return 3 not 0 because it returns the remainder vanesi self.head agadi gayo
            return temp #and the value at 2 was returned
        
    def printCircularQueue(self):
            if(self.head ==-1):
                print("No element in the circular queue")
        
            elif(self.tail >= self.head ):#euta element matrai vayo vane pani yo condition meet garxa, this is when last ma aako item last mai xa i.e at the right of the array
                for i in range(self.head, self.tail +1):#tail +1 kinabhane last to ta include nai hunna so to include that 
                    print(self.queue[i], end = " ")   
                print()

            else:
                for i in range(self.head,self.k):# this is when last ma aako array thau nabhara agadi pugyo 
                    #bichha katai bata last samma print garyo
                    print(self.queue[i],end= " ")
                for i in range(0,self.tail +1):
                    print(self.queue[i],end =" ") 
                    #tespazxi shuru bata bichha samma
                print()  


obj = MyCircularQueue(8)
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



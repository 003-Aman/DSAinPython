'''
Applications of Queue
CPU scheduling, Disk Scheduling
When data is transferred asynchronously between two processes.The queue is used for synchronization. For example: IO Buffers, pipes, file IO, etc
Handling of interrupts in real-time systems.
Call Center phone systems use Queues to hold people calling them in order.
routers and switches in networking
maintaining the playlist in media players
'''
#no rocket science here just follows the fifo rule
#this is using functions only
#actually has a REAR and FRONT pointer but in python we are doing it easy
def create_queue():# when we call this function we create an empty array which will represent our queue
    queue =[]
    return queue# and returns the queue

def check_empty(queue):
    return len(queue)==0 #returns a boolean

def enqueue(queue,item):# adds an item to the last of the queue as it is fifo
    queue.append(item)
    print("Enqueued item: "+ str(item))
    return queue # returns the updated queue

def dequeue(queue,item):
    if check_empty(item):
        return "Queue is empty"
    print("Dequeued item :"+ str(item))
    queue.pop(0)
    return queue

print(enqueue([3],5))    


class Queue:#now we do it using a class queue
    def __init__(self):
        self.queue =[] #anytime an object is created using this class an empty array will represent the queue as shown by constructor

    def check_empty(self):
        return len(self.queue)==0
    
    def enqueue(self,item):
        self.queue.append(item)
        print("Enqueued item: "+ str(item))
        return self.queue
    
    def dequeue(self):
        if check_empty(self):
            return "Queue is empty"
        self.queue.pop(0)


q1= Queue()
q1.dequeue()
print(q1.enqueue(9) )      
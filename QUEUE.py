def create_queue():
    queue =[]
    return queue

def check_empty(queue):
    return len(queue)==0

def enqueue(queue,item):
    queue.append(item)
    print("Enqueued item: "+ str(item))
    return queue

def dequeue(queue,item):
    if check_empty(item):
        return "Queue is empty"
    print("Dequeued item :"+ str(item))
    queue.pop(0)
    return queue

print(enqueue([],5))    


class Queue:
    queue =[]

    def check_empty(self):
        return len(self.queue)==0
    
    def enqueue(self,item):
        self.queue.append(item)
        print("Enqueued item: "+ str(item))
        return self.queue
    
    def dequeue(self):
        if check_empty():
            return "Queue is empty"
        self.queue.pop(0)


q1= Queue()
q1.dequeue()       
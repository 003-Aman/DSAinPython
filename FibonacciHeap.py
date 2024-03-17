#consists of a collection of trees which follow min heap or max heap property
#a node can have more than one children or no children at all
#it has more efficient heap operations than binomial and binary heaps

'''
Collection of trees with each tree following the heap ordinary property
Trees may be in any order in the root list
A pointer to the minimum element of the heap is always maintained
Siblings are connected through a circular doubly linked list
Each child points to its parent
But each parent points to any one child
Degree(x): No of children of nodes of a tree
Mark(x): 1- Lost one of its child(initially all have 0)
         0- Lost no child


'''
#fibonnaci heaps decrease the time complexities of merge,decreasekey

# Fibonacci Heap in python

import math

# Creating fibonacci tree
class FibonacciTree:
    def __init__(self, value):
        self.value = value
        self.child = []#initializes an empty array which stores the child nodes
        self.order = 0 #this represents the no. of children of children at first

    # Adding tree at the end of the tree
    def add_at_end(self, t):
        self.child.append(t)#this appends the value of t that we give in the empty array of the child
        self.order = self.order + 1 #which means no.of children pani increase bhayo


# Creating Fibonacci heap
class FibonacciHeap:# this is the bigger picture of the tree
    def __init__(self):
        self.trees = [] #now this is the heap which stores the inital number of trees of it
        self.least = None # this is a pointer initially points to none but late will point to the minimum element in the heap
        self.count = 0 # represents the no.of nodes in the heap

    # Insert a node
    def insert_node(self, value):
        new_tree = FibonacciTree(value) # inserting a node means initializing a new tree
        self.trees.append(new_tree) # a new tree is created in the above line and added to the empty array of the the self.trees which holds the no. of trees in the heap
        if (self.least is None or value < self.least.value):
            self.least = new_tree # self.least points to the object new node, here if it is the first one to go in obviously it will be the minimum
        self.count = self.count + 1 # count holds the number of trees in the heap, order holds the no.of children these trees have

    # Get minimum value
    def get_min(self):
        if self.least is None:#which means if there are no trees in the heap
            return None
        return self.least.value # return the value of which the self.least is pointing right now

    # Extract the minimum value
    def extract_min(self):
        smallest = self.least #this line stored the current minumum node of the heap in the variable "smallest"
        if smallest is not None: #checks if heap is no empty
            for child in smallest.child: # iterates over each child in the smallest node kinabhane self.least was pointing to the minumum node aba tei bata iterate gardai janxa
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.value

    # Consolidate the tree
    def consolidate(self):
        aux = (floor_log(self.count) + 1) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if (self.least is None
                        or k.value < self.least.value):
                    self.least = k


def floor_log(x):
    return math.frexp(x)[1] - 1


fibonacci_heap = FibonacciHeap()

fibonacci_heap.insert_node(7)
fibonacci_heap.insert_node(3)
fibonacci_heap.insert_node(17)
fibonacci_heap.insert_node(24)

print('the minimum value of the fibonacci heap: {}'.format(fibonacci_heap.get_min()))

print('the minimum value removed: {}'.format(fibonacci_heap.extract_min()))